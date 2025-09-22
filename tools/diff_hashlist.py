import sys

import pandas as pd


def main(current_hash_txt, master_hash_csv, output_txt):
    # 1. 현재 해시 불러오기
    with open(current_hash_txt, "r", encoding="utf-8") as f:
        current = [line.strip().split(maxsplit=1) for line in f if line.strip()]
    current_df = pd.DataFrame(current, columns=["sha256", "path"])

    # 2. 마스터 해시 불러오기 + 컬럼명 통일
    master_df = pd.read_csv(master_hash_csv)
    if "sha256" not in master_df.columns:
        if "file_hash" in master_df.columns:
            master_df.rename(columns={"file_hash": "sha256"}, inplace=True)
        elif "hash" in master_df.columns:
            master_df.rename(columns={"hash": "sha256"}, inplace=True)
        else:
            raise ValueError(
                "❌ master 파일에 'sha256', 'hash', 또는 'file_hash' 컬럼이 없습니다."
            )

    # 3. 병합 및 필요한 파일만 추출
    matched = pd.merge(master_df, current_df, how="inner", on="sha256")

    # 4. 경로만 추출하여 저장
    matched["path"].to_csv(output_txt, index=False, header=False)
    print(f"✅ needed_files.txt 생성 완료: {len(matched)}개 파일")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("사용법: diff_hashlist.py current.txt master.csv output.txt")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
