import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start_date: str, end_date: str, interval: str = "1d", save_csv: bool = True) -> pd.DataFrame:
    """
    Fetch historical stock data from Yahoo Finance using yfinance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        interval (str): Data interval ('1d', '1wk', '1mo', etc.).
        save_csv (bool): Whether to save the data to a CSV.

    Returns:
        pd.DataFrame: DataFrame of historical stock data.
    """
    print(f"Fetching {ticker} from {start_date} to {end_date}...")
    stock = yf.download(ticker, start=start_date, end=end_date, interval=interval)

    if stock.empty:
        print("⚠️ No data found.")
        return stock

    stock.reset_index(inplace=True)

    if save_csv:
        filename = f"data/{ticker}_{interval}_{start_date}_to_{end_date}.csv"
        stock.to_csv(filename, index=False)
        print(f"✅ Data saved to {filename}")

    return stock
