import numpy as np
from PIL import Image
import os

# Caminho da imagem
base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join( "12.jpg")

# Abrir imagem colorida
im = Image.open(path_img).convert("RGB")
r, g, b = im.split()

def equalizar_canal(canal):
    valores = list(canal.getdata())
    counts = np.bincount(valores, minlength=256)
    total_pixels = sum(counts)
    
    # Calcular CDF
    cdf = []
    acumulado = 0
    for contagem in counts:
        acumulado += contagem
        cdf.append(acumulado)
    
    # Gerar novos níveis
    niveis = [int((sk * 255) // total_pixels) for sk in cdf]
    
    # Aplicar equalização
    pixels_equalizados = [niveis[p] for p in valores]
    canal_eq = Image.new("L", canal.size)
    canal_eq.putdata(pixels_equalizados)
    return canal_eq

# Equalizar cada canal
r_eq = equalizar_canal(r)
g_eq = equalizar_canal(g)
b_eq = equalizar_canal(b)

# Combinar os canais equalizados
imagem_eq = Image.merge("RGB", (r_eq, g_eq, b_eq))
imagem_eq.save(os.path.join("imagem_rgb_equalizada_altonivel.jpg"))

print("Imagem colorida equalizada com sucesso.")