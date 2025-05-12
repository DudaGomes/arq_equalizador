# Carregar os dados do histograma equalizado com Assembly
file_path_assembly = "/mnt/data/histograma_equalizador_pb.txt"
hist_assembly = [0] * 256
with open(file_path_assembly, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(' - ')
        if len(parts) == 2:
            pixel_str, freq_str = parts
            pixel = int(pixel_str.replace('Pixel ', '').strip())
            freq = int(freq_str.replace('ocorrencia', '').strip())
            hist_assembly[pixel] = freq

# Plotar histograma equalizado com Assembly
plt.figure(figsize=(12, 6))
plt.bar(range(256), hist_assembly, width=1.0)
plt.title("Histograma Equalizado - Assembly")
plt.xlabel("Valor do Pixel (0-255)")
plt.ylabel("Ocorrência")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
