# History of Probability: Highlights & Simulations

Este repositorio contiene una síntesis académica avanzada y simulaciones computacionales basadas en la conferencia **"Some highlights from the history of probability"** impartida por el **Prof. Yuval Peres** en el *Beijing Institute of Mathematical Sciences and Applications* (BIMSA).

El proyecto conecta la rigurosidad de la teoría de la medida y los hitos históricos de la probabilidad con herramientas modernas de simulación numérica.

---

## 📁 Estructura del Repositorio

El proyecto se encuentra organizado de manera modular para separar la documentación científica del código ejecutable:

```text
├── .gitignore                 # Filtro para evitar subir archivos basura de LaTeX y Python
├── README.md                  # Descripción general del proyecto (este archivo)
├── articulo_yuvalperes/       # Documentación académica formal
│   └── main.tex               # Archivo fuente en LaTeX listo para Overleaf
└── simulaciones_python/       # Código de programación y experimentos
    ├── requirements.txt       # Librerías y dependencias necesarias
    ├── simulacion_borel.py    # Simulación de la normalidad de dígitos (Borel)
    └── simulacion_polya.py    # Caminatas aleatorias y el Teorema de Pólya