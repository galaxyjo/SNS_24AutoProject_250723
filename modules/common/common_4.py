# modules/common/common_4.py (정밀 디버깅 후 전체 스크립트)

def is_even(number: int) -> bool:
    """주어진 숫자가 짝수인지 확인"""
    return number % 2 == 0

def main():
    """테스트용 main 함수"""
    for i in range(5):
        print(f"{i} is even? {is_even(i)}")

if __name__ == "__main__":
    main()
