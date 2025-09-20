import yfinance as yf
import pandas as pd
from config import SYMBOLS_SP500, SYMBOLS_SP500_ASG, PERIODO, INTERVALO

def _descargar(symbols):
    if not symbols:
        raise ValueError("⚠️ La lista de símbolos está vacía. Revisa config.py")

    try:
        data = yf.download(symbols, period=PERIODO, interval=INTERVALO, auto_adjust=True)
    except Exception as e:
        raise ValueError(f"❌ Error al conectarse a Yahoo Finance: {e}")

    if data.empty:
        raise ValueError(f"⚠️ No se pudieron descargar datos para: {symbols}")

    # Normaliza columnas
    if isinstance(data.columns, pd.MultiIndex):
        if "Close" in data.columns.levels[0]:
            precios = data["Close"]
        elif "Adj Close" in data.columns.levels[0]:
            precios = data["Adj Close"]
        else:
            raise ValueError("⚠️ No se encontró columna 'Close' ni 'Adj Close'")
    else:
        if "Close" in data.columns:
            precios = pd.DataFrame(data["Close"])
        elif "Adj Close" in data.columns:
            precios = pd.DataFrame(data["Adj Close"])
        else:
            raise ValueError("⚠️ No se encontró columna 'Close' ni 'Adj Close'")

    precios = precios.dropna()
    if precios.empty:
        raise ValueError(f"⚠️ Todos los datos para {symbols} estaban vacíos después de limpiar NaN")
    precios.columns = [str(c) for c in precios.columns]
    return precios

def obtener_datos_sp500():
    return _descargar(SYMBOLS_SP500)

def obtener_datos_sp500_asg():
    return _descargar(SYMBOLS_SP500_ASG)
