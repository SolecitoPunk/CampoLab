Uso básico
==========

Resolver la ecuación de Laplace:

.. code-block:: python

   from campo_estatico_mdf.laplace_solver import LaplaceSolver2D

   solver = LaplaceSolver2D(n=50, left=0, right=1, top=0, bottom=0)
   V, iterations = solver.solve_jacobi()

Visualizar resultados:

.. code-block:: python

   from campo_estatico_mdf.visual import plot_potential
   fig, ax = plot_potential(V)
