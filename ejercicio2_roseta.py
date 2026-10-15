from PIL import Image
import math


# --------------------------------------------------
# Bresenham 
# --------------------------------------------------
def bresenham(pixels, x0, y0, x1, y1,
              color, ancho, alto):

    dx, dy = abs(x1 - x0), abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    x, y = x0, y0

    while True:

        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color

        if x == x1 and y == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x += sx

        if e2 < dx:
            err += dx
            y += sy


# --------------------------------------------------
# Generar puntos de la circunferencia
# --------------------------------------------------
def generar_puntos_circulo(cx, cy, radio, n):

    puntos = []

    for i in range(n):

        angulo = 2 * math.pi * i / n

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        puntos.append((x, y))

    return puntos


# --------------------------------------------------
# Color con gradiente
# --------------------------------------------------
def obtener_color(i, j, n):

    t = (i + j) / (2 * n)

    r = int(255 * t)
    g = 50
    b = int(255 * (1 - t))

    return (r, g, b)


# --------------------------------------------------
# Dibujar toda la roseta
# --------------------------------------------------
def dibujar_roseta(pixels,
                   puntos,
                   ancho,
                   alto):

    n = len(puntos)

    for i in range(n):

        for j in range(i + 1, n):

            color = obtener_color(i, j, n)

            bresenham(
                pixels,
                puntos[i][0],
                puntos[i][1],
                puntos[j][0],
                puntos[j][1],
                color,
                ancho,
                alto
            )


# --------------------------------------------------
# Crear una variante
# --------------------------------------------------
def generar_roseta(n):

    ancho = 700
    alto = 700

    imagen = Image.new(
        "RGB",
        (ancho, alto),
        "white"
    )

    pixels = imagen.load()

    puntos = generar_puntos_circulo(
        350,
        350,
        300,
        n
    )

    dibujar_roseta(
        pixels,
        puntos,
        ancho,
        alto
    )

    imagen.save(f"roseta_{n}.png")

    print(f"Imagen generada: roseta_{n}.png")


# --------------------------------------------------
# Variantes solicitadas
# --------------------------------------------------
for n in [12, 24, 36]:
    generar_roseta(n)