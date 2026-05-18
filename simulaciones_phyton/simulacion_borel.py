import numpy as np
import matplotlib.pyplot as plt

def simular_ley_logaritmo_iterado(pasos=500000):
    # Generar saltos equiprobables de +1 o -1
    saltos = np.random.choice([-1, 1], size=pasos)
    # Trayectoria acumulada S_n
    S_n = np.cumsum(saltos)
    
    # Definir el dominio temporal n (evitando n <= 2 para el log(log(n)))
    n = np.arange(3, pasos + 1)
    S_n_ajustado = S_n[2:]
    
    # Frontera teórica de Khinchin: sqrt(2 * n * log(log(n)))
    frontera_superior = np.sqrt(2 * n * np.log(np.log(n)))
    frontera_inferior = -frontera_superior
    
    # Graficar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(n, S_n_ajustado, label='$S_n$ (Caminata Aleatoria)', color='blue', alpha=0.7, lw=0.8)
    plt.plot(n, frontera_superior, label='$\pm\sqrt{2n \log \log n}$ (Límite de Khinchin)', color='red', linestyle='--', lw=2)
    plt.plot(n, frontera_inferior, color='red', linestyle='--', lw=2)
    
    plt.title('Simulación Numérica de la Ley del Logaritmo Iterado')
    plt.xlabel('Número de pasos ($n$)')
    plt.ylabel('Posición ($S_n$)')
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle=':', alpha=0.5)
    plt.show()

# Ejecutar simulación estocástica
simular_ley_logaritmo_iterado()