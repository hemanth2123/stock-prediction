import yfinance as yf
from sklearn.linear_model import LinearRegression
import pandas as pd
from datetime import timedelta

def predict_next_day(symbol):
    # Download data
    stock = yf.download(symbol, start="2020-01-01")

    # Prepare features
    stock = stock.dropna()
    stock['Target'] = stock['Close'].shift(-1)
    stock = stock.dropna()

    X = stock[['Close', 'Open', 'High', 'Low', 'Volume']]
    y = stock['Target']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next day
    last_row = stock.iloc[-1]
    latest_data = pd.DataFrame([last_row[X.columns]])
    predicted_price = model.predict(latest_data)[0]

    # Get next date
    last_date = stock.index[-1]
    next_day = last_date + timedelta(days=1)

    return round(predicted_price, 2), next_day.strftime('%Y-%m-%d')
