import os
import matplotlib.pyplot as plt

def graficar_indices(sp500, asg):
    os.makedirs("outputs/graficos", exist_ok=True)
    fig, ax = plt.subplots()
    sp500.mean(axis=1).plot(ax=ax, label="S&P 500", linewidth=2)
    asg.mean(axis=1).plot(ax=ax, label="S&P 500 ASG", linewidth=2)
    ax.legend()
    ax.set_title("Comparación de Índices")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio Promedio")
    plt.tight_layout()
    plt.savefig("outputs/graficos/comparacion_indices.png")
    return fig

def graficar_predicciones(predicciones):
    os.makedirs("outputs/graficos", exist_ok=True)
    fig, ax = plt.subplots()
    predicciones.set_index("Fecha")["Proyeccion"].plot(ax=ax, linewidth=2)
    ax.set_title("Proyección de Precios ASG (ARIMA)")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio Proyectado")
    plt.tight_layout()
    plt.savefig("outputs/graficos/proyeccion_asg.png")
    return fig
