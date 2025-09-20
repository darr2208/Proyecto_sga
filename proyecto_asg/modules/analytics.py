import pandas as pd
import numpy as np

def resumen_rendimiento(sp500, asg):
    resumen = pd.DataFrame({
        "Rentabilidad SP500": sp500.pct_change().mean(),
        "Rentabilidad ASG": asg.pct_change().mean()
    })
    return resumen

def comparar_volatilidad(sp500, asg):
    volatilidad = pd.DataFrame({
        "Volatilidad SP500": sp500.pct_change().std(),
        "Volatilidad ASG": asg.pct_change().std()
    })
    return volatilidad

def calcular_sharpe(sp500, asg, rf=0.02):
    retornos_sp500 = sp500.pct_change()
    retornos_asg = asg.pct_change()
    sharpe_sp500 = (retornos_sp500.mean() - rf/252) / retornos_sp500.std()
    sharpe_asg = (retornos_asg.mean() - rf/252) / retornos_asg.std()
    return pd.DataFrame({"Sharpe SP500": sharpe_sp500, "Sharpe ASG": sharpe_asg})

def calcular_beta(sp500, asg):
    retornos_sp500 = sp500.pct_change().dropna()
    retornos_asg = asg.pct_change().dropna()
    cov = np.cov(retornos_asg.mean(), retornos_sp500.mean())[0][1]
    var = np.var(retornos_sp500.mean())
    beta = cov / var if var != 0 else np.nan
    return beta
