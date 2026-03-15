import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

print("\n=== PRIMEIRAS LINHAS DO DATASET ===")
print(df.head())

df["faturamento"] = df["valor"] * df["quantidade"]

faturamento_total = df["faturamento"].sum()

print("\n=== FATURAMENTO TOTAL ===")
print(f"R$ {faturamento_total}")

faturamento_produto = df.groupby("produto")["faturamento"].sum().sort_values(ascending=False)

print("\n=== FATURAMENTO POR PRODUTO ===")
print(faturamento_produto)

faturamento_cidade = df.groupby("cidade")["faturamento"].sum().sort_values(ascending=False)

print("\n=== FATURAMENTO POR CIDADE ===")
print(faturamento_cidade)

quantidade_produto = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)

print("\n=== QUANTIDADE VENDIDA POR PRODUTO ===")
print(quantidade_produto)

ticket_medio = df["faturamento"].mean()

print("\n=== TICKET MÉDIO ===")
print(f"R$ {ticket_medio:.2f}")

maior_venda = df.loc[df["faturamento"].idxmax()]

print("\n=== MAIOR VENDA ===")
print(maior_venda)

print("\n=== INSIGHTS ===")

produto_top = faturamento_produto.idxmax()
cidade_top = faturamento_cidade.idxmax()

print(f"Produto que mais gerou faturamento: {produto_top}")
print(f"Cidade com maior faturamento: {cidade_top}")
print(f"Ticket médio das vendas: R$ {ticket_medio:.2f}")

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
faturamento_produto.plot(kind="bar")
plt.title("Faturamento por Produto")

plt.subplot(1,3,2)
faturamento_cidade.plot(kind="bar")
plt.title("Faturamento por Cidade")

plt.subplot(1,3,3)
quantidade_produto.plot(kind="bar")
plt.title("Quantidade Vendida")

plt.tight_layout()
plt.show()