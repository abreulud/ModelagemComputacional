# Este arquivo recria a base de dados simulada do projeto.

import pandas as pd

dados = [
    ["Suburbio", 25000, 150, 16.2],
    ["Cajazeiras", 30000, 140, 17.8],
    ["Sao Caetano", 20000, 160, 15.4],
    ["Liberdade", 22000, 155, 16.9],
    ["Periperi", 19000, 135, 18.5],
    ["Paripe", 21000, 145, 17.2],

    ["Brotas", 18000, 310, 10.8],
    ["Itapua", 14000, 290, 11.5],
    ["Cabula", 16000, 270, 12.1],
    ["Federacao", 8000, 300, 10.4],
    ["Rio Vermelho", 9500, 350, 8.9],

    ["Barra", 12000, 480, 6.7],
    ["Pituba", 15000, 510, 5.9],
    ["Caminho das Arvores", 9000, 530, 5.4],
    ["Graca", 7000, 470, 6.3],
    ["Horto Florestal", 6000, 560, 4.8],
    ["Ondina", 7500, 490, 6.1],

    ["CIA - Polo Industrial", 1200, 2800, 7.5],
    ["Comercio", 3500, 1900, 8.1],
    ["Aeroporto", 800, 2200, 6.9],
]

df = pd.DataFrame(
    dados,
    columns=[
        "bairro",
        "num_unidades_consumidoras",
        "consumo_medio_kwh",
        "perda_estimada_pct"
    ]
)

df["consumo_total_kwh"] = (
    df["num_unidades_consumidoras"] * df["consumo_medio_kwh"]
)

df = df[
    [
        "bairro",
        "num_unidades_consumidoras",
        "consumo_medio_kwh",
        "consumo_total_kwh",
        "perda_estimada_pct"
    ]
]

df.to_csv("consumo_energia.csv", index=False, encoding="utf-8")

print("Arquivo consumo_energia.csv criado com sucesso.")
print("Total de bairros:", len(df))
