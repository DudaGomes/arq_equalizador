from PIL import Image
import os

# Caminho da imagem dentro da pasta equalização/imagens
imagem_original = os.path.join("12.jpg")

# Abre a imagem e converte para tons de cinza
img = Image.open(imagem_original).convert("L")

# Salva a imagem convertida com o nome exigido
img.save(os.path.join("Imagem_PB.jpg"))


print("Imagem_PB.jpg salva com sucesso!")


#oi 