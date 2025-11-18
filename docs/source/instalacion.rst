
Instalación
===========

El paquete ``campo_estatico_mdf`` puede instalarse fácilmente usando ``pip``:

Instalación desde PyPI
----------------------

Si el paquete ha sido publicado en PyPI o TestPyPI, simplemente ejecute:

.. code-block:: bash

   pip install campo_estatico_mdf

Instalación desde el repositorio local
--------------------------------------

Si está trabajando con el código fuente:

.. code-block:: bash

   git clone https://github.com/SolecitoPunk/campo_estatico_mdf
   cd campo_estatico_mdf
   pip install -e .

El parámetro ``-e`` (“editable”) permite modificar el código localmente mientras
el paquete sigue siendo accesible desde Python.

Requisitos:

- Python 3.8 o superior
- numpy
- matplotlib
- sphinx (solo para documentación)
- streamlit (para interfaz GUI)

Instalar desde el repositorio local:

.. code-block:: bash

   pip install -e .

Instalar dependencias específicas:

.. code-block:: bash

   pip install numpy matplotlib streamlit
