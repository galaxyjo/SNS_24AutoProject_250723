import argparse
from pathlib import Path

import pandas as pd

"""
Inputs:
 - recent_hash.csv (filename, current_fullpath, sha256)
 - sha256_list.20250723_1618.csv (full_path, sha256)  # baseline
Output:
 - recent_mapping.csv (sha256, filename, current_fullpath, mastertree_target_relpath, match_type, status)
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--recent-hash", required=True, help="Path to recent_hash.csv")
    ap.add_argument(
        "--baseline", required=True, help="Path to sha256_list.20250723_1618.csv"
    )
    ap.add_argument(
        "--project-root",
        required=False,
        default=None,
        help="Root to relativize baseline full_path",
    )
    ap.add_argument("--out", required=True, help="Path to write recent_mapping.csv")
    args = ap.parse_args()

    recent = pd.read_csv(args.recent_hash, encoding="utf-8")
    base = pd.read_csv(args.baseline, encoding="utf-8")

    recent["sha256_norm"] = recent["sha256"].str.strip().str.lower()
    base["sha256_norm"] = base["sha256"].str.strip().str.lower()

    grp = base.groupby("sha256_norm")
    records = []

    for _, r in recent.iterrows():
        h = r["sha256_norm"]
        filename = r.get("filename", Path(str(r["current_fullpath"])).name)
        cur = r["current_fullpath"]
        if h in grp.groups:
            matches = base.loc[grp.groups[h]]
            if len(matches) == 1:
                b = matches.iloc[0]
                base_full = str(b["full_path"])
                if args.project_root:
                    try:
                        rel = str(Path(base_full).relative_to(Path(args.project_root)))
                    except Exception:
                        rel = base_full
                else:
                    rel = base_full
                records.append(
                    {
                        "sha256": r["sha256"],
                        "filename": filename,
                        "current_fullpath": cur,
                        "mastertree_target_relpath": rel,
                        "match_type": "hash",
                        "status": "OK",
                    }
                )
            else:
                candidates = list(matches["full_path"].astype(str).unique())
                records.append(
                    {
                        "sha256": r["sha256"],
                        "filename": filename,
                        "current_fullpath": cur,
                        "mastertree_target_relpath": " || ".join(candidates),
                        "match_type": "hash",
                        "status": "CONFLICT",
                    }
                )
        else:
            records.append(
                {
                    "sha256": r["sha256"],
                    "filename": filename,
                    "current_fullpath": cur,
                    "mastertree_target_relpath": "",
                    "match_type": "none",
                    "status": "NEW",
                }
            )

    out_df = pd.DataFrame.from_records(
        records,
        columns=[
            "sha256",
            "filename",
            "current_fullpath",
            "mastertree_target_relpath",
            "match_type",
            "status",
        ],
    )
    out_df.to_csv(args.out, index=False, encoding="utf-8")
    print(f"✅ Mapping written: {args.out} (rows={len(out_df)})")


if __name__ == "__main__":
    main()
