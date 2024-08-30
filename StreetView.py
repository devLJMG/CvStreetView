import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('C:/Users/User/Downloads/rodovia3d.jpeg')

print("Imagem carregada com sucesso aqui você deve por o caminho de sua imagem em seu explorador de arquivo.")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Aqui ocorre a detecção de pixel que são transformados em escala de cinza")

# Detecção de bordas
edges = cv2.Canny(gray_image, 50, 150)

print("Detecção de bordas após o processamento de escala em cinza.")

# Detecção de linhas usando Transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)

print("Define as linhas de detecção de borda da rodovia.")

# Desenha as linhas detectadas na imagem original
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Exibe a imagem resultante
cv2.imshow('Rodovia Detectada', image)
cv2.waitKey(0)
print("Código de parada")
cv2.destroyAllWindows()
