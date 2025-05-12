from PIL import Image
import numpy as np

def extrair_pixels_em_binario(caminho_imagem, componente='R'):
    # Abrir imagem
    imagem = Image.open(caminho_imagem).convert('RGB')

    # Converter imagem em matriz NumPy (altura x largura x 3)
    matriz_rgb = np.array(imagem)

    # Dicionário para acessar o canal correto
    canais = {'R': 0, 'G': 1, 'B': 2}

    if componente not in canais:
        raise ValueError("Componente inválida. Use 'R', 'G' ou 'B'.")

    # Extrair apenas o canal escolhido
    canal_escolhido = matriz_rgb[:, :, canais[componente]]

    # Converter os valores para binário (8 bits por pixel)
    canal_binario = []
    for valor in canal_escolhido.flatten():
        # Convertendo para binário de 8 bits (0 a 255)
        canal_binario.append(format(valor, '08b'))

    # Salvar os dados binários em um arquivo
    nome_arquivo = f'pixels_{componente}_binario.bin'
    with open(nome_arquivo, 'w') as f:
        for bin_pixel in canal_binario:
            f.write(bin_pixel + '\n')

    print(f'Dados binários salvos em: {nome_arquivo}')
    return canal_binario

# Exemplo de uso
caminho_imagem = '12.jpg'  # Substitua pelo caminho da sua imagem
componente = 'R'  # Escolha entre 'R', 'G' ou 'B' para o canal desejado
extrair_pixels_em_binario(caminho_imagem, componente)
