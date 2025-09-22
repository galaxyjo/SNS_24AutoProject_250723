from modules.auto_generate import runner


def test_generate_data_output_length():
    data = runner.generate_data(42)
    assert len(data) == 5


def test_validate_structure_valid():
    assert runner.validate_structure([1, 2, 3]) is True
