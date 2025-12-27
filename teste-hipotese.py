import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv("ab_data.csv")
print(df.head())

# Criar amostra
df_sample = df.sample(n=5000, random_state=42)
print("Tamanho da amostra:", df_sample.shape[0], "\n")

# Separar grupos
control = df_sample[df_sample["group"] == "control"]
treatment = df_sample[df_sample["group"] == "treatment"]

print("Usuários - Controle:", control.shape[0])
print("Usuários - Tratamento:", treatment.shape[0], "\n")

# Taxa de conversão
taxa_control = control["converted"].mean()
taxa_treatment = treatment["converted"].mean()

print(f"Taxa de conversão (Controle): {taxa_control:.4f}")
print(f"Taxa de conversão (Tratamento): {taxa_treatment:.4f}\n")

# Teste Z bicaudal
conversoes = np.array([
    control["converted"].sum(),
    treatment["converted"].sum()
])

amostras = np.array([
    control.shape[0],
    treatment.shape[0]
])

z_stat, p_value = proportions_ztest(
    count=conversoes,
    nobs=amostras,
    alternative="two-sided"
)

print("Resultado do Teste Z:")
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}\n")

# Conclusão
alpha = 0.05

if p_value < alpha:
    print("Rejeitamos H₀")
    print("Existe diferença estatisticamente significativa entre as versões do site.")
else:
    print("Não rejeitamos H₀")
    print("Não foi encontrada diferença estatisticamente significativa entre as versões.")

# Análise ao longo do tempo

# Converter timestamp para datetime
df_sample["timestamp"] = pd.to_datetime(df_sample["timestamp"])
df_sample["date"] = df_sample["timestamp"].dt.date

# Taxa de conversão por data e grupo
conversao_tempo = (
    df_sample
    .groupby(["date", "group"])["converted"]
    .mean()
    .reset_index()
)

print("\nTaxa de conversão ao longo do tempo (primeiras linhas):")
print(conversao_tempo.head())

# Gráfico temporal
plt.figure()
for g in conversao_tempo["group"].unique():
    subset = conversao_tempo[conversao_tempo["group"] == g]
    plt.plot(subset["date"], subset["converted"], label=g)

plt.xlabel("Data")
plt.ylabel("Taxa de Conversão")
plt.title("Evolução da Taxa de Conversão ao Longo do Tempo")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
