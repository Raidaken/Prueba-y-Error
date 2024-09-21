from turtle import *
from math import *

speed(0)  # Velocidad máxima
bgcolor("black")  # Fondo negro
goto(0, -40)

# Dibujar las hojas
for i in range(16):
    for j in range(18):
        color('#FFA216')
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        left(180)
        circle(40, 24)

# Dibujar el centro de la flor
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')  # Color del centro
golden_ang = 137.508
phi = golden_ang * (pi / 180)

# Utiliza una lista para guardar las posiciones y ángulos
positions = []
for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    positions.append((x, y, i * golden_ang))

# Dibuja todos los estampados
for x, y, angle in positions:
    penup()
    goto(x, y)
    setheading(angle)
    pendown()
    stamp()

# Define points to draw letters
def point(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('#FFA216')
    begin_fill()
    circle(4)
    end_fill()

# Function to draw 'H'
def draw_H(x, y):
    positions_H = [
    (x+10, y + 20), (x+10, y + 15), (x+10,y+10),
    (x+10, y+5), (x+10,y),(x+10, y - 5),
        (x+10, y - 10), (x+10,y-15), (x+10,y-20),
        (x+15,y), (x + 20, y),(x+25,y),
        (x + 30, y + 20), (x + 30, y + 15),
         (x+30,y+10),(x+30,y+5), (x+30, y),
         (x+30,y-5), (x + 30, y - 10),(x+30,y-15),
          (x + 30, y - 20)
    ]

    for pos in positions_H:
        point(*pos)

    # Add the middle line
    penup()
    goto(x, y - 10)
    pendown()
    goto(x + 10, y - 10)

# Function to draw 'I'
def draw_I(x, y):
    positions_I = [
        (x+10, y + 20), (x+10, y + 15),
        (x+10, y + 10),(x+10, y+5), (x+10, y),
         (x+10, y - 5),  (x+10, y - 10), (x+10,y-15), (x+10,y-20)
    ]

    for pos in positions_I:
        point(*pos)

# Move to the center of the flower
penup()
goto(0, -20)
pendown()

# Draw 'HI'
draw_H(-27, 0)
draw_I(10, 0)

hideturtle()
done()