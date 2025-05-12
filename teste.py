from PIL import Image
import os

# Caminho da imagem
path_img = '12.jpg'
im = Image.open(path_img)

def create_bin(nome_arquivo: str):
    # Obtem todos os dados dos pixels (tuplas R,G,B)
    pixels = im.getdata()

    # Converte a sequência de tuplas (R,G,B) em uma lista linear [R, G, B, R, G, B, ...]
    pixel_bytes = bytes([value for pixel in pixels for value in pixel])

    # Garante que o diretório existe
    os.makedirs("./bins", exist_ok=True)

    # Escreve todos os bytes no arquivo binário
    with open(f"./bins/{nome_arquivo}", 'wb') as f:
        f.write(pixel_bytes)

# Cria o arquivo binário combinado
create_bin("frequencias_rgb.bin")