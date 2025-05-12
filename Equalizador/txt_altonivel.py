from collections import Counter

def bin_to_txt(caminho_bin, caminho_txt):
    # Lê os bytes do arquivo binário
    with open(caminho_bin, 'rb') as f:
        dados = f.read()

    # Conta as ocorrências de cada valor de byte
    frequencias = Counter(dados)

    # Escreve todos os valores de 0 a 255 no arquivo .txt (mesmo que com 0 ocorrências)
    with open(caminho_txt, 'w') as f:
        for valor in range(256):
            ocorrencia = frequencias.get(valor, 0)
            f.write(f'Pixel {valor} - ocorrencia {ocorrencia}\n')

# Executa a função no arquivo desejado
bin_to_txt('freque_rgb.bin', 'frequencias_rgb.txt')