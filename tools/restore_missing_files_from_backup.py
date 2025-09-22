import os
import shutil
from pathlib import Path

# 📦 기준 백업 경로
BACKUP_ROOT = Path(r"C:\backup_0914_1738_SNS_24AutoProject_250723")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
failed_files = Path(PROJECT_ROOT / "black_failed_files.txt")

if not failed_files.exists():
    print("❌ 오류 목록 파일이 존재하지 않습니다.")
    exit(1)

print("♻️ 백업 기반 누락 파일 복구 시작...")

restored = 0
missing = 0

for line in failed_files.read_text(encoding="utf-8").splitlines():
    target_path = Path(line.strip())
    if not target_path.exists():
        backup_path = BACKUP_ROOT / target_path.relative_to(PROJECT_ROOT)
        if backup_path.exists():
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(backup_path, target_path)
            print(f"✅ 복구 완료: {target_path}")
            restored += 1
        else:
            print(f"❌ 백업에도 없음: {backup_path}")
            missing += 1

print(f"🔚 복구 완료: {restored}개 | 누락: {missing}개")
