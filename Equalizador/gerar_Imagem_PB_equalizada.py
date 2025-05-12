from PIL import Image
import os

# Caminho para a imagem original PB
base_dir = os.path.dirname(os.path.abspath(__file__))
path_img_pb = os.path.join(base_dir, 'imagens/imagem_PB.jpg')

# Caminho para o arquivo binário equalizado (no mesmo diretório)
path_bin = os.path.join(base_dir, 'bin_bytes_pb.bin')

# Abre a imagem original para pegar as dimensões
img_original = Image.open(path_img_pb)
largura, altura = img_original.size

# Verifica se o arquivo binário existe
if not os.path.exists(path_bin):
    raise FileNotFoundError(f"Arquivo binário não encontrado: {path_bin}")

# Lê os dados binários
with open(path_bin, 'rb') as f:
    bin_data = f.read()

# Cria uma imagem em escala de cinza com os dados
img_equalizada = Image.frombytes('L', (largura, altura), bin_data)

# Salva a imagem
img_equalizada.save(os.path.join(base_dir, 'Imagem_PB_equalizada_assembly.jpg'))