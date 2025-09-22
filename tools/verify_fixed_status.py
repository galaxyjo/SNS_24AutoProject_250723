import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
fixed_files = list(PROJECT_ROOT.rglob("*.fixed.py"))

print("📊 Fixed File 상태 점검 결과:")
for fixed in fixed_files:
    original = fixed.with_name(fixed.name.replace(".fixed.py", ".py"))
    if not original.exists():
        print(f"❌ 원본 없음: {original}")
    else:
        orig_size = os.path.getsize(original)
        fixed_size = os.path.getsize(fixed)
        if orig_size == fixed_size:
            print(f"⚠️ 동일 크기 (수정 의심): {original}")
        else:
            print(f"✅ 수정 완료: {original}")
