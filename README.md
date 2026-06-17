# Projeto Av3 - Consumo de Energia por Bairros de Salvador

Projeto da disciplina de **Modelagem Computacional**.

O objetivo é agrupar bairros/regiões conforme o perfil de consumo de energia elétrica classificando-os por nível de consumo com o objetivo de monitorar quais as regiões predominantes da cidade gastam mais energias.

A técnica usada é **K-Means**, um algoritmo de **aprendizagem não supervisionada**.

A base usada é **simulada**, com 20 bairros da cidade de Salvador. Não há dataset real, então os dados foram criados apenas para demonstrar o funcionamento do algoritmo.

---

## 1. Como abrir no VS Code

1. Abra o VS Code.
2. Clique em `File > Open Folder`.
3. Escolha a pasta do projeto.
4. Abra o terminal do VS Code em `Terminal > New Terminal`.

---

## 2. Criar ambiente virtual

No terminal do VS Code, execute:

```bash
python -m venv venv
```

Depois ative o ambiente virtual.

No Windows:

```bash
venv\Scripts\activate
```

No Linux ou Mac:

```bash
source venv/bin/activate
```

---

## 3. Instalar as bibliotecas

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

---

## 3. Rodar o projeto

No terminal, execute:

```bash
python main.py
```

O programa irá mostrar no terminal:

- total de bairros na base;
- bairros agrupados por tipo de consumo;
- tabela final com os resultados.

Também serão gerados gráficos e arquivos CSV.

---

## 4. Arquivos gerados ao rodar

```bash
resultado_clusters.csv
bairros_por_tipo_consumo.csv
grafico_clusters.png
grafico_quantidade_por_tipo.png
```

---

## 5. Tipos de consumo usados

O projeto separa os bairros em 4 grupos:

- Baixo consumo;
- Consumo médio;
- Alto consumo;
- Grande consumidor.

---

## 6. Variáveis usadas no K-Means

As colunas usadas diretamente no agrupamento são:

- `consumo_medio_kwh`;
- `perda_estimada_pct`.

A coluna `num_unidades_consumidoras` continua na tabela para análise e apresentação, mas não entra diretamente no K-Means nesta versão simplificada.

---

## 7. Explicação simples para apresentação

O projeto usa K-Means para agrupar bairros conforme o perfil de consumo de energia.

Como a base não possui uma classificação pronta, usamos aprendizagem não supervisionada.

O algoritmo analisa o consumo médio e a perda estimada, formando grupos de bairros com características parecidas.

Depois, os grupos são interpretados como baixo consumo, consumo médio, alto consumo e grandes consumidores.

---

> Os dados deste projeto são simulados e foram criados apenas para fins acadêmicos.

