# Projeto Av3 - Consumo de Energia por Bairros

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Ler base de dados
dados = pd.read_csv("consumo_energia.csv")

print("\nBASE DE DADOS CARREGADA:")
print(dados.head())

print("\nTotal de bairros na base:", len(dados))

# 2. Escolher as colunas que serão usadas no agrupamento

colunas_usadas = [
    "consumo_medio_kwh",
    "perda_estimada_pct"
]

x = dados[colunas_usadas]

# 3. Padronizar os dados
padronizador = StandardScaler()
x_padronizado = padronizador.fit_transform(x)

# 4. Aplicar o K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
dados["cluster"] = kmeans.fit_predict(x_padronizado)

# 5. Dar nomes aos grupos
media_por_cluster = dados.groupby("cluster")["consumo_medio_kwh"].mean().sort_values()

nomes_dos_grupos = [
    "Baixo consumo",
    "Consumo medio",
    "Alto consumo",
    "Altíssimo consumo"
]

mapa_nomes = {}

for numero_cluster, nome in zip(media_por_cluster.index, nomes_dos_grupos):
    mapa_nomes[numero_cluster] = nome

dados["tipo_consumo"] = dados["cluster"].map(mapa_nomes)

# 6. Mostrar os bairros de cada tipo de consumo
print("\nBAIRROS AGRUPADOS POR TIPO DE CONSUMO:")

ordem = [
    "Baixo consumo",
    "Consumo medio",
    "Alto consumo",
    "Altíssimo consumo"
]

for tipo in ordem:
    bairros = dados[dados["tipo_consumo"] == tipo]["bairro"].tolist()

    print("\n" + tipo.upper())
    for bairro in bairros:
        print("- " + bairro)

# 7. Salvar resultado em CSV para apresentar
dados_ordenados = dados.sort_values(["tipo_consumo", "bairro"])
dados_ordenados.to_csv("resultado_clusters.csv", index=False, encoding="utf-8")

resumo = (
    dados_ordenados
    .groupby("tipo_consumo")["bairro"]
    .apply(lambda lista: ", ".join(lista))
    .reset_index()
)

resumo["quantidade_bairros"] = resumo["bairro"].apply(lambda texto: len(texto.split(", ")))
resumo.to_csv("bairros_por_tipo_consumo.csv", index=False, encoding="utf-8")

print("\nArquivos gerados:")
print("- resultado_clusters.csv")
print("- bairros_por_tipo_consumo.csv")
print("- grafico_clusters.png")
print("- grafico_quantidade_por_tipo.png")

# 8. Gráfico 1: bairros separados por consumo médio e perda estimada
plt.figure(figsize=(10, 6))

for tipo in ordem:
    grupo = dados[dados["tipo_consumo"] == tipo]
    plt.scatter(
        grupo["consumo_medio_kwh"],
        grupo["perda_estimada_pct"],
        label=tipo
    )

    for _, linha in grupo.iterrows():
        plt.text(
            linha["consumo_medio_kwh"],
            linha["perda_estimada_pct"],
            linha["bairro"],
            fontsize=8
        )

plt.title("Agrupamento dos bairros por perfil de consumo")
plt.xlabel("Consumo médio por unidade consumidora (kWh)")
plt.ylabel("Perda estimada (%)")
plt.legend()
plt.tight_layout()
plt.savefig("grafico_clusters.png", dpi=150)
plt.show()

# 9. Gráfico 2: quantidade de bairros por tipo de consumo
contagem = dados["tipo_consumo"].value_counts().reindex(ordem)

plt.figure(figsize=(8, 5))
plt.bar(contagem.index, contagem.values)
plt.title("Quantidade de bairros por tipo de consumo")
plt.xlabel("Tipo de consumo")
plt.ylabel("Quantidade de bairros")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("grafico_quantidade_por_tipo.png", dpi=150)
plt.show()

# 10. Tabela final
print("\nTABELA FINAL:")
print(dados_ordenados[[
    "bairro",
    "num_unidades_consumidoras",
    "consumo_medio_kwh",
    "perda_estimada_pct",
    "tipo_consumo"
]].to_string(index=False))
