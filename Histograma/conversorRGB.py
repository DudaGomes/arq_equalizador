from PIL import Image
import os

# Diretório do script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho da imagem
img_path = os.path.join(base_dir, '12_equalizada.jpg')

# Abrir imagem
im = Image.open(img_path).convert('RGB')  # Garante RGB

# Pegar todos os bytes (R, G, B sequencialmente)
all_channels = bytes([value for pixel in im.getdata() for value in pixel])

# Salvar tudo em um único arquivo binário
output_path = os.path.join(base_dir, 'freque_rgb.bin')
with open(output_path, 'wb') as f:
    f.write(all_channels)