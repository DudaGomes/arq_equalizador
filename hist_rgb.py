from PIL import Image
import plotly.express as px
import os
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_img = os.path.join("12.jpg")
print(path_img)
#21120
im = Image.open(path_img).convert("RGB")

pixels = list(i for i in im.getdata())
dados = []
for r, g, b in pixels:
    dados.append((r, "Vermelho"))
    dados.append((g, "Verde"))
    dados.append((b, "Azul"))


df = pd.DataFrame(dados, columns=["Intensidade", "Canal"])


fig = px.histogram(
    df,
    x="Intensidade",
    color="Canal",
    nbins=256,
    title="Histograma RGB por Canal",
    color_discrete_map={
    "Vermelho": "rgba(255, 102, 102, 0.6)",  # rosa claro
    "Verde":    "rgba(144, 238, 144, 0.6)",  # verde claro
    "Azul":     "rgba(173, 216, 230, 0.6)",  # azul claro
}
)
fig.show()