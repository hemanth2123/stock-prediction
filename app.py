from flask import Flask, render_template, request
from model import predict_next_day  # ⬅ Import the function
import datetime

app = Flask(__name__)

stocks = {
    "IRCTC": "IRCTC.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "IRFC": "IRFC.NS",
    "BEL": "BEL.NS",
    "HAL": "HAL.NS",
    "Mazagon Dock": "MAZDOCK.NS",
    "RVNL": "RVNL.NS",
    "Titagarh Wagons": "TWL.NS",
    "Vedanta": "VEDL.NS",
    "Reliance": "RELIANCE.NS"  # ✅ Added
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    predicted_date = None
    selected_symbol = None

    if request.method == 'POST':
        selected_symbol = request.form['symbol']
        prediction, predicted_date = predict_next_day(selected_symbol)

    return render_template("index.html", stocks=stocks,
                           prediction=prediction,
                           predicted_date=predicted_date,
                           selected_symbol=selected_symbol)
