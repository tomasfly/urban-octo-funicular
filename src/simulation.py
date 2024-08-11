from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_strategy():    
    data = pd.read_csv('./resources/sp500.csv', index_col='Date', parse_dates=['Date'])
    data['SMA'] = data['SP500'].rolling(window=50).mean()
    data['SMA'] = data['SP500'].rolling(window=100).mean()
    data['Position'] = np.where(data['SP500'] > data['SMA'], 1, 0)
    data['Position'] = data['Position'].shift()
    data['StrategyPct'] = data['SP500'].pct_change(1) * data['Position']
    data['Strategy'] = (data['StrategyPct'] + 1).cumprod()
    data['BuyHold'] = (data['SP500'].pct_change(1) + 1).cumprod()
    data[['Strategy', 'BuyHold']].plot()
    plt.show()
