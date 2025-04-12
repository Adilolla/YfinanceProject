import pandas as pd

def add_sma(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean()
    return df

def add_ema(df: pd.DataFrame, span: int = 20) -> pd.DataFrame:
    df[f"EMA_{span}"] = df["Close"].ewm(span=span, adjust=False).mean()
    return df

def add_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    ema_12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema_12 - ema_26
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    return df
