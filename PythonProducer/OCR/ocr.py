import cv2
import pytesseract

def carregar_imagem(nome_arquivo):
    return cv2.imread(nome_arquivo)

def desenhar_retangulos(imagem, rois):
    imagem_com_rois = imagem.copy()
    cor = (0, 255, 0)  # Cor dos retângulos (verde)
    espessura = 2      # Espessura da linha do retângulo

    for roi in rois:
        cv2.rectangle(imagem_com_rois, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), cor, espessura)

    return imagem_com_rois

def extrair_texto(imagem, roi):
    texto = pytesseract.image_to_string(imagem[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]])
    return texto

def processar_imagem(nome_arquivo, rois):
    # Carregue a imagem do cartão de crédito
    imagem_cartao = carregar_imagem(nome_arquivo)

    # Desenhe retângulos delimitadores ao redor das ROIs na imagem
    imagem_com_rois = desenhar_retangulos(imagem_cartao, rois)

    # Extraia texto de cada ROI usando o Tesseract OCR
    textos = [extrair_texto(imagem_cartao, roi) for roi in rois]

    return imagem_com_rois, textos
