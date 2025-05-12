import os
from collections import Counter

def bin_to_txt(nome_bin, nome_txt):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório onde o script está
    caminho_bin = os.path.join(base_dir, nome_bin)
    caminho_txt = os.path.join(base_dir, nome_txt)

    with open(caminho_bin, 'rb') as f:
        dados = f.read()

    frequencias = Counter(dados)

    with open(caminho_txt, 'w') as f:
        for valor in range(256):
            ocorrencia = frequencias.get(valor, 0)
            f.write(f'Pixel {valor} - Ocorrencia {ocorrencia}\n')

# Chamada segura
bin_to_txt('freque_rgb.bin', 'frequencias_rgb_equalizada.txt')