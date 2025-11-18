Notas teóricas
==============

La ecuación de Laplace en 2D se define como:

.. math::

   \nabla^2 V = 
   \frac{\partial^2 V}{\partial x^2} + 
   \frac{\partial^2 V}{\partial y^2} = 0

El método de diferencias finitas aproxima las derivadas como:

.. math::

   V_{i,j} =
   \frac{1}{4} \left(
   V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1}
   \right)
