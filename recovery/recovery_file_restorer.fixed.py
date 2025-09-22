
os.makedirs(os.path.dirname(old_path), exist_ok=True)
            results.append(f"✅ 복원: {new_path} → {old_path}")
            results.append(f"❌ 실패: {new_path} → {old_path} | {str(e)}")
            shutil.copy2(new_path, old_path)
        except Exception as e:
        try:
    for old_path, new_path, _ in renamed_list:
    results = []
    return results
# recovery/recovery_file_restorer.py
def restore_files(renamed_list):
import os
import shutil

pass
