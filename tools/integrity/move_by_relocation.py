# tools/integrity/move_by_relocation.py
import argparse
import csv
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# === 하드코딩 경로(요청사항) ===
BACKUP_ROOT = r"C:\backup\SNS_24AutoProject_FINAL_20250516_1002"
PROJECT_ROOT = r"C:\SNS_24AutoProject_250723"


def de_bom(s: str) -> str:
    return s.lstrip("\ufeff").strip() if isinstance(s, str) else s


def norm_sep(p: str) -> str:
    return p.replace("\\", os.sep).replace("/", os.sep)


def norm_source(src_raw: str) -> str:
    src = de_bom(src_raw)
    src = src.replace("<MAY_BACKUP_ROOT>", BACKUP_ROOT)
    src = norm_sep(src)
    return os.path.normpath(src)


def resolve_target(tgt_raw: str) -> str:
    tgt = de_bom(tgt_raw)
    # <PROJECT_ROOT> 치환
    if "<PROJECT_ROOT>" in tgt:
        tgt = tgt.replace("<PROJECT_ROOT>/", "").replace("<PROJECT_ROOT>\\", "")
        tgt = norm_sep(tgt).lstrip(os.sep)
        out = os.path.join(PROJECT_ROOT, tgt)
    else:
        # 절대경로면 그대로, 아니면 PROJECT_ROOT 기준
        if os.path.isabs(tgt):
            out = tgt
        else:
            out = os.path.join(PROJECT_ROOT, norm_sep(tgt).lstrip(os.sep))
    return os.path.normpath(out)


def ensure_parent(dir_or_file: str) -> None:
    Path(dir_or_file).parent.mkdir(parents=True, exist_ok=True)


def load_mapping(json_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # 필수 키 방어
    norm = []
    for it in data:
        if not isinstance(it, dict):
            continue
        if "source" in it and "target" in it:
            norm.append(
                {
                    "source": it["source"],
                    "target": it["target"],
                    "mode": it.get("mode", "copy"),
                    "note": it.get("note", ""),
                }
            )
    return norm


def write_log(logdir: str, rows):
    Path(logdir).mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    out = os.path.join(logdir, f"restore_log_{ts}.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "target", "status", "note"])
        w.writerows(rows)
    print(f"[LOG] Saved to {out}")


def move_files(mapping, dry_run: bool):
    rows = []
    ok = skip = fail = 0
    for it in mapping:
        src = norm_source(it["source"])
        dst = resolve_target(it["target"])

        if not os.path.exists(src):
            rows.append((src, dst, "FAIL", "Source not found"))
            fail += 1
            continue

        if dry_run:
            rows.append((src, dst, "DRY-RUN", "Simulated copy"))
            skip += 1
            continue

        try:
            ensure_parent(dst)
            shutil.copy2(src, dst)
            rows.append((src, dst, "OK", "Copied"))
            ok += 1
        except Exception as e:
            rows.append((src, dst, "FAIL", str(e)))
            fail += 1

    total = len(mapping)
    print(f"[SUMMARY] total={total} ok={ok} skip={skip} fail={fail}")
    return rows


def prune_missing(mapping, out_json_path: str):
    kept, missing = [], []
    for it in mapping:
        src_resolved = norm_source(it["source"])
        if os.path.exists(src_resolved):
            kept.append(it)
        else:
            m = dict(it)
            m["_resolved_source"] = src_resolved
            missing.append(m)

    # 결과 저장
    ensure_parent(out_json_path)
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(kept, f, ensure_ascii=False, indent=2)

    miss_csv = out_json_path.replace(".json", "_missing.csv")
    with open(miss_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "resolved_source"])
        for m in missing:
            w.writerow([m["source"], m["_resolved_source"]])

    print(f"[PRUNE] kept={len(kept)} missing={len(missing)}")
    print(f"[PRUNE] json -> {out_json_path}")
    print(f"[PRUNE] missing list -> {miss_csv}")


def main():
    ap = argparse.ArgumentParser(description="Relocation executor with prune support")
    ap.add_argument("--json", required=True, help="Mapping JSON path")
    ap.add_argument("--dry-run", action="store_true", help="Simulate copy")
    ap.add_argument("--execute", action="store_true", help="Do real copy")
    ap.add_argument(
        "--logdir", default=os.path.join(PROJECT_ROOT, "logs"), help="Log dir"
    )
    ap.add_argument(
        "--prune-missing",
        action="store_true",
        help="Build _ready.json with existing sources only",
    )
    args = ap.parse_args()

    mapping = load_mapping(args.json)

    if args.prune_missing:

        base = os.path.splitext(args.json)[0]
        out_json = base + "_ready.json"
        prune_missing(mapping, out_json)
        return

    # 실행 플래그 없으면 안전하게 dry-run
    dry = True if (not args.execute) else False

    rows = move_files(mapping, dry_run=dry)
    write_log(args.logdir, rows)


if __name__ == "__main__":
    main()
