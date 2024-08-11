import pandas as pd
import matplotlib.pyplot as plt

def plot_sp500():
    data = pd.read_csv('./resources/sp500.csv', index_col='Date', parse_dates=['Date'])
    data['SMA'] = data['SP500'].rolling(window=50).mean()
    data.plot()
    plt.show()