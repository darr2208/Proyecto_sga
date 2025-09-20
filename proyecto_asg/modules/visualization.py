import matplotlib.pyplot as plt

def graficar_indices(sp500, asg):
    sp500.mean(axis=1).plot(label="S&P 500", linewidth=2)
    asg.mean(axis=1).plot(label="S&P 500 ASG", linewidth=2)
    plt.legend()
    plt.title("Comparación de Índices")
    plt.xlabel("Fecha")
    plt.ylabel("Precio Promedio")
    plt.tight_layout()
    plt.savefig("outputs/graficos/comparacion_indices.png")
    plt.close()

def graficar_predicciones(predicciones):
    predicciones.set_index("Fecha")["Proyeccion"].plot(linewidth=2)
    plt.title("Proyección de Precios ASG (ARIMA)")
    plt.xlabel("Fecha")
    plt.ylabel("Precio Proyectado")
    plt.tight_layout()
    plt.savefig("outputs/graficos/proyeccion_asg.png")
    plt.close()
