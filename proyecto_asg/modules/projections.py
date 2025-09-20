import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def predecir_precio(asg, metodo="ARIMA"):
    if metodo == "ARIMA":
        serie = asg.mean(axis=1).dropna()
        modelo = ARIMA(serie, order=(1,1,1))
        ajuste = modelo.fit()
        pred = ajuste.get_forecast(steps=30)
        return pd.DataFrame({
            "Fecha": pred.row_labels,
            "Proyeccion": pred.predicted_mean
        })
    return pd.DataFrame()
