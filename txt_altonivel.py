from collections import Counter

def bin_to_txt(caminho_bin, caminho_txt):
    # Lê os bytes do arquivo .bin
    with open(caminho_bin, 'rb') as f:
        pixel_bytes = f.read()

    # Conta as ocorrências de cada valor (0 a 255)
    frequencias = Counter(pixel_bytes)

    # Escreve as frequências no arquivo .txt
    with open(caminho_txt, 'w') as f:
        for i, (valor_pixel, ocorrencia) in enumerate(frequencias.items(), start=1):
            f.write(f'Pixel {i} - ocorrencia {ocorrencia}\n')

# Exemplo de uso
bin_to_txt('./bins/frequencias_rgb.bin', 'frequencias_rgb.txt')