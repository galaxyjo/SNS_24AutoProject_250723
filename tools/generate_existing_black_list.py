# tools/generate_existing_black_list.py

from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "black_failed_files.txt"
output_file = project_root / "black_failed_files_existing.txt"

existing = []

with input_file.open("r", encoding="utf-8") as f:
    for line in f:
        path = line.strip()
        if not path or path.startswith("#"):
            continue
        p = project_root / path if not Path(path).is_absolute() else Path(path)
        if p.exists():
            existing.append(str(p.relative_to(project_root)))

with output_file.open("w", encoding="utf-8") as f:
    for path in existing:
        f.write(path + "\n")

print(f"✅ 존재하는 파일 {len(existing)}개 → {output_file.name} 저장 완료")
