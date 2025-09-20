import yfinance as yf
import pandas as pd
from config import SYMBOLS_SP500, SYMBOLS_SP500_ASG, PERIODO, INTERVALO

def _descargar(symbols):
    data = yf.download(symbols, period=PERIODO, interval=INTERVALO, auto_adjust=True)

    # Si hay múltiples columnas y son MultiIndex, selecciona "Close"
    if isinstance(data.columns, pd.MultiIndex):
        if "Close" in data.columns.levels[0]:
            precios = data["Close"]
        elif "Adj Close" in data.columns.levels[0]:
            precios = data["Adj Close"]
        else:
            raise KeyError("No se encontró columna 'Close' ni 'Adj Close' en los datos descargados.")
    else:
        # Si es un único símbolo, convierte en DataFrame
        if "Close" in data.columns:
            precios = pd.DataFrame(data["Close"])
        elif "Adj Close" in data.columns:
            precios = pd.DataFrame(data["Adj Close"])
        else:
            raise KeyError("No se encontró columna 'Close' ni 'Adj Close' en los datos descargados.")

    precios = precios.dropna()
    precios.columns = [str(c) for c in precios.columns]
    return precios

def obtener_datos_sp500():
    return _descargar(SYMBOLS_SP500)

def obtener_datos_sp500_asg():
    return _descargar(SYMBOLS_SP500_ASG)
