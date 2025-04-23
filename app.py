from flask import Flask, render_template, request
import yfinance as yf
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']

    # Download latest data
    stock = yf.download(ticker, start="2020-01-01")

    # Create target column
    stock['Target'] = stock['Close'].shift(-1)
    stock.dropna(inplace=True)

    X = stock[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = stock['Target']

    # Train/Test Split
    X_train = X[:-1]
    y_train = y[:-1]

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict next day using last row
    last_row = X.iloc[[-1]]
    predicted_price = model.predict(last_row)[0]

    return render_template('result.html', prediction=round(predicted_price, 2), ticker=ticker)

if __name__ == '__main__':
    app.run(debug=True)
