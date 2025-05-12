from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__)) # caminho para o arquivo da imagem
path_img = os.path.join(base_dir, '12.jpg')  # substitua pelo nome correto da sua imagem

im = Image.open(path_img) # abrir imagem

frequencia_green = [i[1] for i in im.getdata()]  # extrair os dados da tupla, pegando os valores de G
bytes_green = bytes(frequencia_green)  # 'bytes' converte para bytes puros

with open("freque_green.bin", "wb") as f: # escrever os dados no arquivo bin
    f.write(bytes_green)


