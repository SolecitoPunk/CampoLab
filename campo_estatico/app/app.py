import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from campo_estatico_mdf.laplace_solver import LaplaceSolver2D

# -----------------------------
# Tema visual tipo GitHub Dark
# -----------------------------
st.set_page_config(
    page_title="CampoLab – Simulador MDF",
    layout="wide",
    page_icon="⚡",
)

# -----------------------------
# CABECERA CON LOGO + TÍTULO
# -----------------------------
col1, col2 = st.columns([1, 8])
with col1:
   import os
BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "logo.png")
st.image(logo_path, width=90)
 # colócale tu logo
with col2:
    st.markdown(
        """
        # ⚡ CampoLab  
        ### Simulación del campo eléctrico con la ecuación de Laplace (MDF)
        Un entorno interactivo para explorar potenciales y campos eléctricos.
        """
    )

st.divider()

# -----------------------------
# SIDEBAR CONTROLES
# -----------------------------
st.sidebar.header("🔧 Parámetros de simulación")

n = st.sidebar.slider("Tamaño de malla (n x n)", 10, 200, 50)
tolerancia = st.sidebar.number_input("Tolerancia", min_value=1e-10, value=1e-4, format="%e")
max_iters = st.sidebar.number_input("Máx. iteraciones", min_value=100, value=5000)

st.sidebar.subheader("Condiciones de contorno (Voltajes)")
izq = st.sidebar.number_input("Izquierda", value=0.0)
der = st.sidebar.number_input("Derecha", value=10.0)
sup = st.sidebar.number_input("Superior", value=5.0)
inf = st.sidebar.number_input("Inferior", value=0.0)

st.sidebar.subheader("Método numérico")
metodo = st.sidebar.selectbox(
    "Método de resolución",
    ["Jacobi", "Gauss-Seidel"]
)

st.sidebar.subheader("Opciones gráficas")
mostrar_campo = st.sidebar.checkbox("Mostrar campo eléctrico (flechas)", True)
densidad = st.sidebar.slider("Densidad del campo", 5, 50, 20)

animar = st.sidebar.checkbox("Animar iteraciones", False)

run_sim = st.sidebar.button("🚀 Ejecutar simulación")

# -----------------------------
# FUNCIÓN AUXILIAR PARA GRAFICAR
# -----------------------------
def graficar_resultados(V, E_x=None, E_y=None, titulo="Potencial eléctrico"):
    fig, ax = plt.subplots(figsize=(6, 5))
    plt.title(titulo)

    cmap = ListedColormap(plt.cm.coolwarm(np.linspace(0, 1, 256)))

    img = ax.imshow(V, cmap=cmap, origin="lower")
    plt.colorbar(img, ax=ax, fraction=0.045)

    if E_x is not None and E_y is not None:
        skip = (slice(None, None, densidad), slice(None, None, densidad))
        ax.quiver(
            E_y[skip],
            -E_x[skip],
            color="black",
            alpha=0.8,
            scale=80
        )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")

    return fig

# -----------------------------
# EJECUCIÓN DE LA SIMULACIÓN
# -----------------------------
if run_sim:

    solver = LaplaceSolver2D(n=n, tolerancia=tolerancia)
    solver.establecer_condiciones_contorno(
        izquierda=izq,
        derecha=der,
        superior=sup,
        inferior=inf,
    )

    st.subheader("⚙ Cálculo en progreso...")

    # Animación iterativa (opcional)
    if animar:
        paso = max(1, max_iters // 10)

        frames = []

        v_old = solver.v.copy()

        frames = []
        v_original = solver.v.copy()

        for k in range(paso, max_iters + 1, paso):
            # Restaurar estado base para evitar acumulación
            solver.v[:] = v_original

            if metodo == "Jacobi":
                solver.resolver_jacobi(max_iteraciones=k)
            else:
                solver.resolver_gauss_seidel(max_iteraciones=k)

            frames.append(solver.v.copy())


            frames.append(solver.v.copy())

        st.write("### 🌀 Animación de convergencia")

        for i, frame in enumerate(frames):
            fig = graficar_resultados(frame, None, None,
                                      titulo=f"Iteración {i * paso}")
            st.pyplot(fig)
            plt.close()

    # Ejecución final
    if metodo == "Jacobi":
        iteraciones = solver.resolver_jacobi(max_iteraciones=max_iters)
    else:
        iteraciones = solver.resolver_gauss_seidel(max_iteraciones=max_iters)

    V = solver.obtener_potencial()
    E_x, E_y = solver.calcular_campo_e()

    st.success(f"Convergencia alcanzada en **{iteraciones} iteraciones** ✔️")

    # Resultados
    colA, colB = st.columns([2, 3])

    with colA:
        st.write("### 🔋 Potencial eléctrico (V)")
        fig = graficar_resultados(V)
        st.pyplot(fig)

    with colB:
        if mostrar_campo:
            st.write("### 🧭 Campo eléctrico (E)")
            fig2 = graficar_resultados(V, E_x, E_y, titulo="Campo eléctrico")
            st.pyplot(fig2)

    st.divider()

    st.write("### 📥 Exportar datos")
    st.download_button(
        "Descargar matriz de potencial",
        data="\n".join([" ".join(map(str, row)) for row in V]),
        file_name="potencial.txt"
    )

else:
    st.info("Ajusta los parámetros en la barra lateral y presiona **Ejecutar simulación**.")
