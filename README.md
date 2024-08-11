
- [`main.py`](./main.py): Entry point of the application.
- [`resources/sp500.csv`](./resources/sp500.csv): CSV file containing S&P 500 data.
- [`src/plotdata.py`](./src/plotdata.py): Contains the function to read and plot the S&P 500 data.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```sh
    pip install pandas matplotlib
    ```

## Usage

Run the following command to plot the S&P 500 data:
```sh
python main.py
```

## Running Tests

To run the unit tests, use the following command:

```sh
python -m unittest discover -s tests
```

