from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join(base_dir + '12.jpg')

im = Image.open("12.jpg")

frequencia_blue = list(i[2] for i in im.getdata())
bytes_blue = bytes(frequencia_blue)

with open("freque_blue.bin", 'wb') as f:
    f.write(bytes_blue)