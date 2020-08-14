import pandas as pd


def load_data():
    """
    Bond movie data in pandas dataframe format.
    """
    url = "https://raw.githubusercontent.com/andrew-block/jamesbond/master/data/data.csv"
    df = pd.read_csv(url)

    return df
