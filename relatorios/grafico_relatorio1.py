# Calcula o histograma real a partir dos valores individuais dos pixels
unique, counts = np.unique(data, return_counts=True)
hist_data = dict(zip(unique, counts))

# Gera o vetor de frequência de 0 a 255
histogram = [hist_data.get(i, 0) for i in range(256)]

# Plota o histograma
plt.figure(figsize=(12, 6))
plt.bar(range(256), histogram, width=1.0)
plt.title("Histograma Original do Canal Vermelho (Imagem QCIF)")
plt.xlabel("Valor do Pixel (0-255)")
plt.ylabel("Ocorrência")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
