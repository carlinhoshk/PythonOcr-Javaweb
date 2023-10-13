from OCR import ocr
import cv2
# Defina manualmente as coordenadas das três ROIs (x, y, largura, altura)
roi1 = (40, 350, 410, 60)   # Exemplo de ROI 1
roi2 = (40, 450, 300, 50)   # Exemplo de ROI 2
roi3 = (40, 560, 170, 40)   # Exemplo de ROI 3

imagem_com_rois, textos = ocr.processar_imagem('data/cpf.jpg', [roi1, roi2, roi3])

# Exiba a imagem com os retângulos delimitadores
cv2.imshow('Imagem com ROIs', imagem_com_rois)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exiba o texto extraído de cada ROI
print("\nTexto da ROI 1:")
print(textos[0])

print("\nTexto da ROI 2:")
print(textos[1])

print("\nTexto da ROI 3:")
print(textos[2])
