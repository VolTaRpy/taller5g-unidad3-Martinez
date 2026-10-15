from PIL import Image
import math


# --------------------------------------------------
# Algoritmo DDA 
# --------------------------------------------------
def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una linea usando el algoritmo DDA."""
    dx, dy = x1 - x0, y1 - y0
    pasos = max(abs(dx), abs(dy))

    if pasos == 0:
        return

    x_inc, y_inc = dx / pasos, dy / pasos

    x, y = x0, y0

    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)

        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color

        x += x_inc
        y += y_inc


# --------------------------------------------------
# Rectángulo
# --------------------------------------------------
def dibujar_rectangulo(pixels, x0, y0, x1, y1,
                       color, ancho, alto):

    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


# --------------------------------------------------
# Triángulo
# --------------------------------------------------
def dibujar_triangulo(pixels, p1, p2, p3,
                      color, ancho, alto):

    dda(pixels, p1[0], p1[1], p2[0], p2[1],
        color, ancho, alto)

    dda(pixels, p2[0], p2[1], p3[0], p3[1],
        color, ancho, alto)

    dda(pixels, p3[0], p3[1], p1[0], p1[1],
        color, ancho, alto)


# --------------------------------------------------
# Sol con rayos
# --------------------------------------------------
def dibujar_sol(pixels, cx, cy, radio,
                n_rayos, color, ancho, alto):

    for i in range(n_rayos):

        angulo = i * 2 * math.pi / n_rayos

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        dda(pixels, cx, cy, x, y,
            color, ancho, alto)


# --------------------------------------------------
# Programa principal
# --------------------------------------------------
ancho = 600
alto = 500

imagen = Image.new("RGB",
                   (ancho, alto),
                   (200, 230, 255))

pixels = imagen.load()

# Piso
dda(
    pixels,
    0, 400,
    599, 400,
    (0, 120, 0),
    ancho, alto
)

# Casa principal
dibujar_rectangulo(
    pixels,
    180, 200,
    420, 400,
    (150, 75, 0),
    ancho, alto
)

# Techo
dibujar_triangulo(
    pixels,
    (150, 200),
    (300, 100),
    (450, 200),
    (220, 0, 0),
    ancho, alto
)

# Puerta
dibujar_rectangulo(
    pixels,
    270, 280,
    330, 400,
    (100, 50, 0),
    ancho, alto
)

# Ventana izquierda
dibujar_rectangulo(
    pixels,
    220, 240,
    270, 290,
    (0, 0, 255),
    ancho, alto
)

# Ventana derecha
dibujar_rectangulo(
    pixels,
    330, 240,
    380, 290,
    (0, 0, 255),
    ancho, alto
)

# Sol
dibujar_sol(
    pixels,
    80, 80,
    60,
    8,
    (255, 215, 0),
    ancho, alto
)

imagen.save("casa.png")

print("Imagen generada: casa.png")