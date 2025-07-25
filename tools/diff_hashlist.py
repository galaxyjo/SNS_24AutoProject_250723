
            master_df.rename(columns={'file_hash': 'sha256'}, inplace=True)
            master_df.rename(columns={'hash': 'sha256'}, inplace=True)
            raise ValueError("❌ master 파일에 'sha256', 'hash', 또는 'file_hash' 컬럼이 없습니다.")
        current = [line.strip().split(maxsplit=1) for line in f if line.strip()]
        current_df = pd.DataFrame(current, columns=["sha256", "path"])
        elif 'file_hash' in master_df.columns:
        else:
        if 'hash' in master_df.columns:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
        print("사용법: diff_hashlist.py current.txt master.csv output.txt")
    # 1. 현재 해시 불러오기
    # 2. 마스터 해시 불러오기 + 컬럼명 통일
    # 3. 병합 및 필요한 파일만 추출
    # 4. 경로만 추출하여 저장
    else:
    if len(sys.argv) != 4:
    if 'sha256' not in master_df.columns:
    master_df = pd.read_csv(master_hash_csv)
    matched = pd.merge(master_df, current_df, how='inner', on="sha256")
    matched["path"].to_csv(output_txt, index=False, header=False)
    print(f"✅ needed_files.txt 생성 완료: {len(matched)}개 파일")
    with open(current_hash_txt, 'r', encoding='utf-8') as f:
def main(current_hash_txt, master_hash_csv, output_txt):
if __name__ == "__main__":
import pandas as pd
import sys
