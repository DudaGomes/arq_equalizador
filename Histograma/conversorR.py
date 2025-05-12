from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join(base_dir + '12.jpg')

im = Image.open("12.jpg")

frequencia_red = list(i[0] for i in im.getdata())
bytes_red = bytes(frequencia_red)

with open("freque_red.bin", 'wb') as f:
    f.write(bytes_red)