import yfinance as yf

data = yf.download("NTPC", period="1mo")

print(data)