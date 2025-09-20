import yfinance as yf
import pandas as pd
from config import SYMBOLS_SP500, SYMBOLS_SP500_ASG, PERIODO, INTERVALO

def _descargar(symbols):
    data = yf.download(symbols, period=PERIODO, interval=INTERVALO, group_by="ticker", auto_adjust=True)
    if isinstance(symbols, list) and len(symbols) > 1:
        precios = pd.concat([data[ticker]["Close"] for ticker in symbols], axis=1)
        precios.columns = symbols
    else:
        # Si es un solo símbolo, se devuelve como DataFrame con una sola columna
        precios = pd.DataFrame(data["Close"])
        precios.columns = [symbols if isinstance(symbols, str) else symbols[0]]
    return precios.dropna()

def obtener_datos_sp500():
    return _descargar(SYMBOLS_SP500)

def obtener_datos_sp500_asg():
    return _descargar(SYMBOLS_SP500_ASG)
