
          .query("filename.str.endswith('.py')", engine="python"))
    master.rename(columns={'hash': 'sha256'}, inplace=True)
    master.rename(columns={'SHA256': 'sha256'}, inplace=True)
    master.rename(columns={'해시': 'sha256'}, inplace=True)
    raise KeyError("❌ 'sha256' 컬럼 없음. 열 이름을 확인하세요.")
# ▼ 경로 수정 필요시 여기를 바꾸세요
# 1. 현재 py 파일 해시 목록 불러오기
# 2. master 기준 해시 목록 불러오기
# 3. 🔍 열 이름 확인 출력
# 4. 컬럼명 맞추기
# 5. py 확장자만 + 해시 일치하는 파일만 필터링
# 6. 결과 저장
cur = pd.read_csv(CUR_LIST, names=["filename", "sha256"])
CUR_LIST = r"C:\clean_rebuild\logs\trace\c_pyroot_file_list_250627_024.txt"
elif 'SHA256' in master.columns:
elif '해시' in master.columns:
else:
from pathlib import Path
if 'hash' in master.columns:
import pandas as pd
master = pd.read_csv(MASTER_CSV, low_memory=False)
MASTER_CSV = r"C:\master_hash_cleaned_final.csv"
needed = (cur[cur["sha256"].isin(master["sha256"])]
OUT_TXT = r"C:\clean_rebuild\needed_files.txt"
Path(OUT_TXT).write_text("\n".join(needed["filename"]))
print("[DEBUG] master.csv columns:", master.columns.tolist())
print(f"[✅ OK] {len(needed)} files → {OUT_TXT}")
