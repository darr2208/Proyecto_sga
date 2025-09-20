from modules import fetcher, analytics, projections, visualization, report

def main():
    datos_sp500 = fetcher.obtener_datos_sp500()
    datos_sp500_asg = fetcher.obtener_datos_sp500_asg()

    resumen = analytics.resumen_rendimiento(datos_sp500, datos_sp500_asg)
    volatilidad = analytics.comparar_volatilidad(datos_sp500, datos_sp500_asg)

    proyecciones_asg = projections.predecir_precio(datos_sp500_asg, metodo="ARIMA")

    visualization.graficar_indices(datos_sp500, datos_sp500_asg)
    visualization.graficar_predicciones(proyecciones_asg)

    report.generar_pdf(resumen, volatilidad, proyecciones_asg)

if __name__ == "__main__":
    main()
