
found = True
            print(f"⚠️ 충돌 위험 파일 발견: {full_path}")
        full_path = os.path.join(target_dir, filename)
        if os.path.exists(full_path):
        print("✅ 충돌 위험 없음")
    "config.py",
    "copy.py",
    "datetime.py",
    "email.py",
    "hashlib.py",
    "json.py",
    "logging.py",
    "math.py",
    "pickle.py",
    "pyarrow.py",
    "random.py",
    "re.py",
    "secrets.py",
    "socket.py",
    "ssl.py",
    "string.py",
    "subprocess.py",
    "time.py",
    "types.py",
    for filename in conflicting_names:
    found = False
    if not found:
    print("🔍 모듈 이름 충돌 검사 시작")
    scan_conflicting_files()
# 검사 대상 폴더
# 실무 기준 최신 충돌 가능 모듈명 목록 (2025 최신 반영)
]
conflicting_names = [
def scan_conflicting_files():
if __name__ == "__main__":
import os

target_dir = r"C:\SNS_24AutoProject\modules"

pass
