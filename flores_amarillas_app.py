import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle

# Configuración de la página web
st.set_page_config(page_title="Un ramo para ti 💐", page_icon="🌻", layout="centered")

st.title("💐 Crea tu propio ramo de flores amarillas")
st.write("Mueve los controles de abajo para personalizar el ramo y envíaselo a alguien especial.")

# --- BARRA LATERAL (controles interactivos) ---
st.sidebar.header("Personaliza el regalo")

# Control para la cantidad de flores
num_flowers = st.sidebar.slider ("Cantidad de flores:", min_value=3, max_value=15, value=11, step=1)

# Selector de color para el papel
paper_color_option = st.sidebar.selectbox(
    "Color del papel de envoltorio:",
    ("Rosa Pastel", "Rosa Fuerte", "Azul Cielo", "Lavanda", "Kraft / Natural")
)

# Diccionario de colores para el papel
colors_dict = {
    "Rosa Pastel": ("#ffb6c1", "#ffc0cb"),
    "Rosa Fuerte": ("#f06292", "#ec407a"),
    "Azul Cielo": ("#bbdefb", "#90caf9"),
    "Lavanda": ("#e1bee7", "#ce93d8"),
    "Kraft / Natural": ("#d7ccc8", "#bcaaa4")
}
p_color_front, p_color_back = colors_dict[paper_color_option]

# Mensaje personalizado por mí
custom_message = "Te amo mucho amor, este ramo es para ti 🩷 "

# --- GENERAR EL DIBUJO ---
fig, ax = plt.subplots(figsize=(7,8))
ax.set_facecolor('#fff9fb')

# 1. Dibujar tallos
np.random.seed(42)
for _ in range(num_flowers + 5):
    start_x = np.random.uniform(-0.6, 0.6)
    start_y = np.random.uniform(0.4, 1.3)
    ax.plot([start_x, 0], [start_y, -1.9], color='#33691e', linewidth=2.2, alpha=0.8)

# 2. Papel de envoltorio
paper_back = Polygon([(-1.2, 0.8), (1.2, 0.8), (0.4, -2.1),(-0.4, -2.1)],
                     color=p_color_back, alpha=0.6, lw=1.5)
paper_front = Polygon([(-1.1, 0.7), (1.1, 0.7), (0.35, -2.2), (-0.35, -2.2)],
                      color=p_color_front, alpha=0.9, lw=2)
ax.add_patch(paper_back)
ax.add_patch(paper_front)

# Lazo
ribbon = Polygon([(-0.35, -1.4), (0.35, -1.4), (0.25, -1.65), (-0.25, -1.65)],
                 color='#ad1457', ec='#880e4f', lw=1.5)
ax.add_patch(ribbon)

# 3. Función para dibujar flores
def draw_flower(cx, cy, scale=1.0, is_sunflower=False):
    angles = np.linspace(0, 2 * np.pi, 14, endpoint=False)
    r = 0.22 * scale
    petal_color = '#ffeb3b' if not is_sunflower else '#ffc107'
    edge_color = '#ffa000'

    for angle in angles:
        x = cx + r * np.cos(angle)
        y = cy + r * np.sin(angle)
        circle = Circle((x,y), 0.2 * scale, color=petal_color, ec=edge_color, alpha=0.9)
        ax.add_patch(circle)

    center_color = '#3e2723' if is_sunflower else '#ff8f00'
    center = Circle ((cx, cy), 0.11 * scale, color=center_color)
    ax.add_patch(center)

# Coordenadas base para las flores
base_positions = [
    (0.0, 1.8, 1.15, True), (-0.5, 1.5, 0.9, False), (0.5, 1.6, 0.95, False),
    (-0.25, 2.2, 0.85, False), (0.35, 2.1, 0.9, True), (-0.8, 1.9, 0.8, False),
    (0.8, 1.8, 0.8, False), (0.0, 2.45, 0.85, False), (-0.4, 1.0, 0.9, True),
    (0.4, 1.1, 0.85, False), (0.0,1,35, 1.0, False), (-0.6, 2.3, 0.75, False),
    (0.6, 2.2, 0.75, True), (0.0, 2.8, 0.7, False), (-0.2, 0.7, 0.8, False)
]

#Dibujar solo la cantidad de flores que el usuario eligió
for i in range(min(num_flowers, len(base_positions))):
    fx, fy, fs, is_sun = base_positions[i]
    draw_flower(fx, fy, fs, is_sun)

ax.set_xlim(-2.0, 2.0)
ax.set_ylim(-2.5, 3.3)
ax.axis('off')

# Mostrar el mensaje personalizado mío
if custom_message:
    plt.title(custom_message, fontsize=13, color='#ad1457', fontweight='bold', pad=10)

# Mostrar la figura en Streamlit
st.pyplot(fig)
plt.close(fig)
