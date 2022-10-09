import os
import random
from time import sleep

os.system('cls')

# Introduccion de datos
width = int(input("Introduzca el ancho del laberinto: "))
height = int(input("Introduzca el alto del laberinto: "))
obs = int(input("Introduzca la cantidad de obstaculos: "))
points = int(input("Numero de puntos: "))


while obs > (width * height * 0.8):
    nval = int(input("Error, la cantidad de paredes no debe ocupar más que el 80% del laberinto: "))
    obs = nval
maze = []

# Se crea el terreno
for i in range(height):
    row = []
    for j in range(width):
        row.append("#")
    maze.append(row)


# Se recorre el laberinto aleatoriamente vacianddo espacios
space = (width * height) - obs
n = 1
x = random.randint(0, width - 1)
y = random.randint(0, height - 1)
maze[y][x] = " "
# Esto se hace hasta que se cumpla la cantidad de espacios correspondiente
while n < space:
    mov = random.randint(0, 3)
    if mov == 0:
        cant = random.randint(0, height - 1 - y)
        for i in range(cant):
            if(n >= space):
                break
            y += 1
            if(maze[y][x] != " "):
                 maze[y][x] = " "
                 n += 1

    if mov == 1:
        cant = random.randint(0, y)
        for i in range(cant):
            if(n >= space):
                break
            y -= 1
            if(maze[y][x] != " "):
                 maze[y][x] = " "
                 n += 1

    if mov == 2:
        cant = random.randint(0, width - 1 - x)
        for i in range(cant):
            if(n >= space):
                break
            x += 1
            if(maze[y][x] != " "):
                 maze[y][x] = " "
                 n += 1

    if mov == 3:
        cant = random.randint(0, x)
        for i in range(cant):
            if(n >= space):
                break
            x -= 1
            if(maze[y][x] != " "):
                 maze[y][x] = " "
                 n += 1


count = 0
while count <= points:
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    if maze[y][x] != "#":
        print("a")
        maze[y][x] = "o"
        count += 1

# Se agrega el objeto movible
while True:
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    if maze[y][x] != "#":
        maze[y][x] = "*"
        break

count_points = 0
position_vis = []
count_time = 0

while True:
    os.system('cls')

    # Se define un movimiento aleatorio
    mov = random.randint(0, 3)

    # Se dibuja el laberinto
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j] + " ", end="")
        print("\n")

    obstaculos = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "#":
                obstaculos += 1
    #print(str(obstaculos) + " paredes")

    if(count_time == 5):
        position_vis = []
    else:
        count_time += 1

    # Se realiza el movimiento
    if y != 0 and mov == 0:
        if maze[y - 1][x] == "o":
            count_points += 1
        if maze[y - 1][x] != "#" and not [x, y] in position_vis:
            position_vis.append([x, y])
            maze[y][x] = " "
            y -= 1
            maze[y][x] = "*"

    if y != height - 1 and mov == 1:
        if maze[y + 1][x] == "o":
            count_points += 1
        if maze[y + 1][x] != "#" and not [x, y] in position_vis:
            position_vis.append([x, y])
            maze[y][x] = " "
            y += 1
            maze[y][x] = "*"
        
    if x != 0 and mov == 2:
        if maze[y][x - 1] == "o":
            count_points += 1
        if maze[y][x - 1] != "#" and not [x, y] in position_vis:
            position_vis.append([x, y])
            maze[y][x] = " "
            x -= 1
            maze[y][x] = "*" 

    if x != width - 1 and mov == 3:
        if maze[y][x + 1] == "o":
            count_points += 1
        if maze[y][x + 1] != "#" and not [x, y] in position_vis:
            position_vis.append([x, y])
            maze[y][x] = " "
            x += 1
            maze[y][x] = "*"

    if count_points >= points:
        break
        
    print("Points earned: " + str(count_points))
    sleep(0.15)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
St