import pandas as pd
import matplotlib.pyplot as plt

def plot_price_with_indicators(df: pd.DataFrame, ticker: str):
    plt.figure(figsize=(14, 7))
    plt.plot(df["Date"], df["Close"], label="Close", color="black", linewidth=1)
    
    if "SMA_20" in df.columns:
        plt.plot(df["Date"], df["SMA_20"], label="SMA 20", linestyle='--')
    if "EMA_20" in df.columns:
        plt.plot(df["Date"], df["EMA_20"], label="EMA 20", linestyle=':')
    
    plt.title(f"{ticker} Price with Indicators")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_rsi(df: pd.DataFrame):
    if "RSI" not in df.columns:
        return
    plt.figure(figsize=(14, 3))
    plt.plot(df["Date"], df["RSI"], label="RSI", color="purple")
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title("RSI")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_macd(df: pd.DataFrame):
    if "MACD" not in df.columns or "Signal" not in df.columns:
        return
    plt.figure(figsize=(14, 3))
    plt.plot(df["Date"], df["MACD"], label="MACD", color="blue")
    plt.plot(df["Date"], df["Signal"], label="Signal", color="orange")
    plt.axhline(0, color='black', linestyle='--')
    plt.title("MACD")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
