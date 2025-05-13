from PIL import Image
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
path_img_pb = os.path.join(base_dir, 'imagens/imagem_PB.jpg')

path_bin = os.path.join(base_dir, 'bin_bytes_pb.bin')
img_original = Image.open(path_img_pb)
largura, altura = img_original.size

# verifica se o arquivo existe
if not os.path.exists(path_bin):
    raise FileNotFoundError(f"Arquivo binário não encontrado: {path_bin}")

# ler binários
with open(path_bin, 'rb') as f:
    bin_data = f.read()

#cria escala de cinza
img_equalizada = Image.frombytes('L', (largura, altura), bin_data)
img_equalizada.save(os.path.join(base_dir, 'Imagem_PB_equalizada_assembly.jpg'))