import cv2
import numpy as np

imagem = cv2.imread("objetos.jpg")

azulClaro = np.array([255,120,30], dtype="uint8")
azulEscuro = np.array([80,30,0], dtype="uint8")

objeto = cv2.inRange(imagem, azulEscuro, azulClaro)

cv2.imshow("nova", objeto)
cv2.waitKey(0)