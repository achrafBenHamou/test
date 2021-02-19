import pytest
import ex_04


@pytest.mark.parametrize(
    "scenario",
    [
        (
            (
                [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3],
                [1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1],
            ),
            ([2, 1, 1, 1, 2, 2, 2, 1], [2, 1, 1, 1, 2, 2, 2, 1]),
        ),
        (
            (
                [1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1],
                [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3],
            ),
            ([1, 1, 2, 2, 2, 1, 1, 1, 2, 2], [1, 1, 2, 2, 2, 1, 1, 1, 3, 3]),
        ),
        (
            (
                [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0],
            ),
            ([1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3], [0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2]),
        ),
        (
            (
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0],
                [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3],
            ),
            ([0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2], [1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3]),
        ),
    ],
)
def test_synchronize(scenario):
    input_list, output_list = scenario
    result = ex_04.synchronize(input_list[0], input_list[1])
    assert result == output_list