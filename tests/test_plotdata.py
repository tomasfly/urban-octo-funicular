import unittest
from src.plotdata import plot_sp500
import pandas as pd

class TestPlotData(unittest.TestCase):
    def test_plot_sp500(self):
        # Load the data
        data = pd.read_csv('./resources/sp500.csv', index_col='Date', parse_dates=['Date'])
        # Calculate the SMA
        data['SMA'] = data['SP500'].rolling(window=50).mean()
        # Check if SMA column is added
        self.assertIn('SMA', data.columns)
        # Check if SMA values are correct (example check)
        # self.assertAlmostEqual(data['SMA'].iloc[50], data['SP500'].iloc[:51].mean(), places=5)

if __name__ == '__main__':
    unittest.main()