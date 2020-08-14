import pytest
from jamesbond import bonddata


def test_load_data():
    """
    Test the row & column count (shape)
    Test the first column from the last row of the dataset 'Spectre'.
    """
    df = bonddata.load_data()
    shape = df.shape
    last_row_first_col = df.iloc[-1, 1]
    assert shape == (24, 27)
    assert last_row_first_col == 'Spectre'
