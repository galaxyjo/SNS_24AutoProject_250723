def generate_data(seed: int) -> list:
    """자동 테스트 데이터를 생성"""
    import random

    random.seed(seed)
    return [random.randint(1, 100) for _ in range(5)]


def validate_structure(data: list) -> bool:
    return all(isinstance(x, int) for x in data)
