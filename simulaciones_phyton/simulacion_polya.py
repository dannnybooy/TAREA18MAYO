import numpy as np

def evaluar_probabilidad_retorno(dimension, pasos_maximos=5000, iteraciones=1000):
    retornos_exitosos = 0
    
    for _ in range(iteraciones):
        # Inicializar vector de posición en el origen
        posicion = np.zeros(dimension, dtype=int)
        
        for t in range(pasos_maximos):
            # Seleccionar una dimensión aleatoria para el movimiento
            eje_movimiento = np.random.randint(0, dimension)
            # Seleccionar dirección (+1 o -1)
            direccion = np.random.choice([-1, 1])
            
            # Actualizar coordenada
            posicion[eje_movimiento] += direccion
            
            # Verificar condición de parada: retorno al origen geométrico
            if np.all(posicion == 0):
                retornos_exitosos += 1
                break
                
    probabilidad_estimada = retornos_exitosos / iteraciones
    return probabilidad_estimada

# Ejecución del análisis comparativo dimensional
print("=== Análisis de Monte Carlo para el Teorema de Pólya ===")
prob_2d = evaluar_probabilidad_retorno(dimension=2, pasos_maximos=10000, iteraciones=500)
print(f"Probabilidad empírica de retorno en 2D (Plano): {prob_2d:.4f} (Teóricamente tiende a 1.00)")

prob_3d = evaluar_probabilidad_retorno(dimension=3, pasos_maximos=10000, iteraciones=500)
print(f"Probabilidad empírica de retorno en 3D (Espacio): {prob_3d:.4f} (Teóricamente tiende a ~0.34)")