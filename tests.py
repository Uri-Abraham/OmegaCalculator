import pytest
from Main import main_tests


@pytest.mark.parametrize("input_data, expected_output", [
    ("63-56", 7),
    ("52*(1$4&6-(--4*36))  ", -7280),
    # Add more test cases as needed
])
def test_your_main_function(input_data, expected_output):
    result = main_tests(input_data)
    assert result == expected_output
