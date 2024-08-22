import pandas as pd


def get_returns(file):
    """
    Get returns from file.
    """
    returns = pd.read_csv('./resources/'+file+'.csv', index_col=0, parse_dates=True).pct_change()
    return returns