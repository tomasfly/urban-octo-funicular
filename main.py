from matplotlib import pyplot as plt
from src.correlationgraph import get_returns
from src.plotdata import plot_sp500
from src.simulation import plot_strategy

if __name__ == "__main__":
    # plot_sp500()
    # plot_strategy()
    df = get_returns('sp500')
    df['NDX'] = get_returns('NDX')
    df['SP500'].rolling(50).corr(df['NDX']).plot()
    plt.show()
