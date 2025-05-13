from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__)) 
path_img = os.path.join(base_dir, '12.jpg') 
im = Image.open(path_img)

frequencia_green = [i[1] for i in im.getdata()] 
bytes_green = bytes(frequencia_green) 

with open("freque_green.bin", "wb") as f: 
    f.write(bytes_green)


