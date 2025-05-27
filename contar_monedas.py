import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('monedas.jpg')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur(gris, 5)

# HoughCircles con parámetros ajustados
circulos = cv2.HoughCircles(gris,
                            cv2.HOUGH_GRADIENT,
                            dp=1.2,
                            minDist=300,
                            param1=100,
                            param2=50,     # AUMENTADO para filtrar más
                            minRadius=300,  # Tamaño mínimo esperado de una moneda
                            maxRadius=370)  # Tamaño máximo esperado

output = img.copy()
conteo = 0

if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    for i, circulo in enumerate(circulos[0, :], start=1):
        # Dibujar el círculo exterior
        cv2.circle(output, (circulo[0], circulo[1]), circulo[2], (0, 255, 0), 2)
        # Dibujar el centro del círculo
        cv2.circle(output, (circulo[0], circulo[1]), 2, (0, 0, 255), 3)
        
        # Añadir etiqueta numérica
        cv2.putText(output, str(i), 
                    (circulo[0] - 10, circulo[1] + 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1.5,  # Tamaño de fuente
                    (255, 0, 0),  # Color azul
                    3)  # Grosor del texto
        
        conteo += 1

print(f"Monedas detectadas: {conteo}")

# Mostrar imagen
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Monedas Detectadas")
plt.axis('off')
plt.show()