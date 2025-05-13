from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(base_dir, '12_equalizada.jpg')

im = Image.open(img_path).convert('RGB') 
# pegar todos os bytes 
all_channels = bytes([value for pixel in im.getdata() for value in pixel])

output_path = os.path.join(base_dir, 'freque_rgb.bin')
with open(output_path, 'wb') as f:
    f.write(all_channels)