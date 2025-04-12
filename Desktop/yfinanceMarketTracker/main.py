import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from fetch_data import fetch_stock_data
from src.indicators import add_sma, add_ema, add_rsi, add_macd
from visualize import plot_price_with_indicators, plot_rsi, plot_macd


if __name__ == "__main__":
    df = fetch_stock_data("AAPL", "2022-01-01", "2023-01-01")
    df = add_sma(df, 20)
    df = add_ema(df, 20)
    df = add_rsi(df)
    df = add_macd(df)

    plot_price_with_indicators(df, "AAPL")
    plot_rsi(df)
    plot_macd(df)
