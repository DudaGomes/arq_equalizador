from PIL import Image
import os

# Caminho para a imagem PB
base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join(base_dir, 'imagem_PB.jpg')

# Abre a imagem
im = Image.open(path_img)

# Gera o binário com os valores de intensidade da imagem PB
def create_bin_pb(nome_arquivo: str):
    grayscale_values = list(i for i in im.getdata())
    pixel_bytes = bytes(grayscale_values)
    
    with open(f'./bins/{nome_arquivo}', 'wb') as f:
        f.write(pixel_bytes)

# Chamada da função
create_bin_pb('freque_pb.bin')