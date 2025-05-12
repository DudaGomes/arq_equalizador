from PIL import Image
import os
with open("bin_bytes_red.bin", "rb") as fr:
        dados_r = list(fr.read())
with open("bin_bytes_green.bin", "rb") as fg:
        dados_g = list(fg.read())
with open("bin_bytes_blue.bin", "rb") as fb:
        dados_b = list(fb.read())

novos_pixels = []
for i in range(21120):
    novos_pixels.append((dados_r[i], dados_g[i], dados_b[i]))

nova_imagem = Image.new("RGB", (176, 120))
nova_imagem.putdata(novos_pixels)
nova_imagem.show()