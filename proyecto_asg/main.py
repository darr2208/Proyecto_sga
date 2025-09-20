import os
from modules import fetcher, analytics, projections, visualization, report

def main():
    try:
        datos_sp500 = fetcher.obtener_datos_sp500()
        datos_sp500_asg = fetcher.obtener_datos_sp500_asg()
    except ValueError as e:
        print(f"Error al descargar datos: {e}")
        return

    if datos_sp500.empty or datos_sp500_asg.empty:
        print("No se obtuvieron datos para uno de los índices. Revisa los símbolos en config.py.")
        return

    os.makedirs("outputs/graficos", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    resumen = analytics.resumen_rendimiento(datos_sp500, datos_sp500_asg)
    volatilidad = analytics.comparar_volatilidad(datos_sp500, datos_sp500_asg)
    sharpe = analytics.calcular_sharpe(datos_sp500, datos_sp500_asg)

    proyecciones_asg = projections.predecir_precio(datos_sp500_asg, metodo="ARIMA")

    fig1 = visualization.graficar_indices(datos_sp500, datos_sp500_asg)
    fig2 = visualization.graficar_predicciones(proyecciones_asg)

    report.generar_pdf(resumen, volatilidad, proyecciones_asg)

    print("Análisis completado. Resultados guardados en carpeta 'outputs'.")

if __name__ == "__main__":
    main()
