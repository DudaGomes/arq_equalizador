import numpy as np
from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join(base_dir, "12.jpg")

# Abrir imagem em tons de cinza
im = Image.open(path_img).convert("L")  # Apenas um canal

# 1. Calcular histograma
valores = list(im.getdata())
counts = np.bincount(valores, minlength=256)
total_pixels = sum(counts)

# 2. Calcular CDF
cdf = []
acumulado = 0
for contagem in counts:
    acumulado += contagem
    cdf.append(acumulado)

# 3. Gerar novos níveis de intensidade
niveis = [int((sk * 255) // total_pixels) for sk in cdf]

# 4. Aplicar equalização
pixels_equalizados = [niveis[p] for p in valores]
imagem_equalizada = Image.new("L", im.size)
imagem_equalizada.putdata(pixels_equalizados)

# 5. Salvar imagem equalizada
imagem_equalizada.save(os.path.join("Imagem_PB_equalizada_altonivel.jpg"))
print("Imagem equalizada salva com sucesso.")

# 6. Salvar histograma
with open("histograma_equalizado_altonivel.txt", "w") as file:
    for pixel, qtd in enumerate(np.bincount(pixels_equalizados, minlength=256)):
        file.write(f"Pixel {pixel} - ocorrencia {qtd}\n")

print("Histograma salvo com sucesso.")
