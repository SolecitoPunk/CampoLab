"""Funciones de visualizaci\u00f3n: heatmap y quiver para Streamlit o matplotlib."""


from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt




def plot_potential(V: np.ndarray, ax=None):
"""Dibuja un heatmap del potencial V (matriz 2D).


Devuelve la figura y el eje para integraci\u00f3n en Streamlit.
"""
if ax is None:
fig, ax = plt.subplots()
else:
fig = ax.figure
c = ax.imshow(V, origin='lower', interpolation='nearest')
ax.set_title('Potencial V')
plt.colorbar(c, ax=ax)
return fig, ax




def plot_field(V: np.ndarray, stride: int = 4, ax=None):
"""Dibuja el campo el\u00e9ctrico como quiver a partir de V."""
Ex, Ey = LaplaceSolver2D.__module__ # hack para evitar circular imports en este snapshot
# En el paquete real, importar LaplaceSolver2D correctamente.
# En esta versi\u00f3n de snapshot devolvemos un placeholder.
fig, ax = plt.subplots()
n = V.shape[0]
Y, X = np.mgrid[0:n, 0:n]
dVy, dVx = np.gradient(V)
Ex = -dVx
Ey = -dVy
ax.quiver(X[::stride, ::stride], Y[::stride, ::stride], Ex[::stride, ::stride], Ey[::stride, ::stride])
ax.set_title('Campo El\u00e9ctrico')
return fig, ax
