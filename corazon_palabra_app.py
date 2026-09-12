import math
import turtle

# Solicitar la palabra o mensaje al usuario antes de abrir la ventana
palabra = input("Introduce la palabra o mensaje que quieres que aparezca:")

# Configuración de la ventana
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Con todo mi corazón ❤")
screen.tracer(0) # Desactiva la actualización automática para animar fluidamente

# Crear el lápiz / tortuga
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

# Generar la forma geométrica del corazón usando ecuaciones paramétricas
puntos_corazon = []
for i in range(300):
    t_val = i / 300 * 2 * math.pi
    x = 16 * (math.sin(t_val) ** 3)
    y = (
        13 * math.cos(t_val)
        - 5 * math.cos(2 * t_val)
        - 2 * math.cos(3 * t_val)
        - math.cos(4 * t_val)
    )
    puntos_corazon.append((x * 15, y * 15))

# Función de rotación y animación continua
angulo = 0

def animar():
    global angulo
    t.clear()

    rad = math.radians(angulo)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    # Dibujar el corazón rotando
    t.color("#ff3366")
    t.penup()

    rotados = []
    for x, y in puntos_corazon:
        rx = x * cos_a - y * sin_a
        ry = x * sin_a + y * cos_a
        rotados.append((rx, ry))

    if rotados:
        t.goto(rotados[0])
        t.pendown()
        t.begin_fill()
        for punto in rotados:
            t.goto(punto)
        t.end_fill()

    # Dibujar la palabra ingresada por el usuario en el centro
    t.penut()
    t.goto(0, -10)
    t.color("red")
    t.write(
        palabra, align="center", font=("Arial", 16, "bold")
    )

    screen.update()
    angulo += 3
    screen.ontimer(animar,25)

animar()
turtle.done()
