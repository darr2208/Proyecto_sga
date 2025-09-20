import yfinance as yf
from config import SYMBOLS_SP500, SYMBOLS_SP500_ASG, PERIODO, INTERVALO

def obtener_datos_sp500():
    return yf.download(SYMBOLS_SP500, period=PERIODO, interval=INTERVALO)["Adj Close"]

def obtener_datos_sp500_asg():
    return yf.download(SYMBOLS_SP500_ASG, period=PERIODO, interval=INTERVALO)["Adj Close"]
