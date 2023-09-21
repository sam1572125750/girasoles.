import turtle as tur
tur.setup(width=800, height=600)

# Ajusta la posición inicial de la ventana
startX = 1000
startY = 1000
tur.setworldcoordinates(-startX, -startY, startX, startY)
tur.bgcolor("darkgrey")
tur.speed(50)  # Establece la velocidad de dibujo

# Función para dibujar la flor
def dibujar_flor():
    tur.penup()
    tur.left(90)
    tur.fd(100)
    tur.pendown()
    tur.right(90)

    tur.fillcolor("yellow")
    tur.begin_fill()
    tur.circle(10, 180)
    tur.circle(25, 110)
    tur.left(50)
    tur.circle(60, 45)
    tur.circle(20, 170)
    tur.right(24)
    tur.fd(30)
    tur.left(10)
    tur.circle(30, 110)
    tur.fd(20)
    tur.left(40)
    tur.circle(90, 70)
    tur.circle(30, 150)
    tur.right(30)
    tur.fd(15)
    tur.circle(80, 90)
    tur.left(15)
    tur.fd(45)
    tur.right(165)
    tur.fd(20)
    tur.left(155)
    tur.circle(150, 80)
    tur.left(50)
    tur.circle(150, 90)
    tur.end_fill()

    tur.left(150)
    tur.circle(-90, 70)
    tur.left(20)
    tur.circle(75, 105)
    tur.setheading(60)
    tur.circle(80, 98)
    tur.circle(-90, 40)

    tur.left(180)
    tur.circle(90, 40)
    tur.circle(-80, 98)
    tur.setheading(-83)

    tur.fd(30)
    tur.left(90)
    tur.fd(25)
    tur.left(45)
    tur.fillcolor("dark green")
    tur.begin_fill()
    tur.circle(-80, 90)
    tur.right(90)
    tur.circle(-80, 90)
    tur.end_fill()
    tur.right(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(85)
    tur.left(90)
    tur.fd(80)

    tur.right(90)
    tur.right(45)
    tur.fillcolor("green")
    tur.begin_fill()
    tur.circle(80, 90)
    tur.left(90)
    tur.circle(80, 90)
    tur.end_fill()
    tur.left(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(60)
    tur.right(90)
    tur.circle(200, 60)

# Configura el número de filas y columnas de flores
num_filas = 1
num_columnas = 10

# Espacio entre flores
espacio_x = 120
espacio_y = 120

# Dibuja las flores en filas y columnas
for fila in range(num_filas):
    for columna in range(num_columnas):
        x = columna * espacio_x - num_columnas * espacio_x / 2
        y = fila * espacio_y - num_filas * espacio_y / 2
        tur.penup()
        tur.goto(x, y)
        dibujar_flor()

# Agregar texto
tur.penup()
tur.goto(0, 310)  # Posición donde deseas agregar el texto
tur.pendown()
tur.color("black")  # Color del texto
tur.write("PARA TI FEAAA!!", align="center", font=("Stencil", 45, "italic"))

# Cierra la ventana al hacer clic en ella
tur.exitonclick()
