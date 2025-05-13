from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "bin_bytes_red.bin"), "rb") as fr:
    dados_r = list(fr.read())

with open(os.path.join(base_dir, "bin_bytes_green.bin"), "rb") as fg:
    dados_g = list(fg.read())

with open(os.path.join(base_dir, "bin_bytes_blue.bin"), "rb") as fb:
    dados_b = list(fb.read())

# reconstruir os pixels
novos_pixels = [(dados_r[i], dados_g[i], dados_b[i]) for i in range(len(dados_r))]

# dimensões da imagem
largura, altura = 176, 120
nova_imagem = Image.new("RGB", (largura, altura))
nova_imagem.putdata(novos_pixels)

saida_path = os.path.join(base_dir, "imagem_rgb_equalizada_assembly.jpg")
nova_imagem.save(saida_path)
print(f"Imagem reconstruída salva em: {saida_path}")