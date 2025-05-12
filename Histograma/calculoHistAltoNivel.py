import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def calcular_histograma(imagem_path):
    imagem = Image.open(imagem_path)
    imagem_rgb = imagem.convert('RGB')    #converter pra rgb
    imagem_array = np.array(imagem_rgb)   # converter pro array

   
    histograma_r = np.histogram(imagem_array[:,:,0], bins=256, range=(0, 256))[0] #calculo hist r
    histograma_g = np.histogram(imagem_array[:,:,1], bins=256, range=(0, 256))[0] #calculo hist g
    histograma_b = np.histogram(imagem_array[:,:,2], bins=256, range=(0, 256))[0] #calculo hist b

    return histograma_r, histograma_g, histograma_b

def plotar_histograma(histograma, canal):
    # gráfico para os canais
    plt.figure(figsize=(10, 6))
    if canal == 'R':
        plt.plot(histograma, color='red')
        plt.title('Histograma do Canal Vermelho (R)')
    elif canal == 'G':
        plt.plot(histograma, color='green')
        plt.title('Histograma do Canal Verde (G)')
    else:
        plt.plot(histograma, color='blue')
        plt.title('Histograma do Canal Azul (B)')
    
    plt.xlabel('Intensidade dos Pixels')
    plt.ylabel('Frequência')

    # exibe e continua apos fechar a primeira janela 
    plt.show()

def main(imagem_path):
    histograma_r, histograma_g, histograma_b = calcular_histograma(imagem_path)

    #grafico r
    plotar_histograma(histograma_r, 'R')

    plotar_histograma(histograma_g, 'G')

    plotar_histograma(histograma_b, 'B')
    
# imagem
imagem_path = '12.jpg'
main(imagem_path)
