import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

df = pd.read_excel('BaseDados.xlsx', header = 0)
df_acima_30 = df[df["Atendimentos"] > 30]
def contar_dias_acima_30(df):
    return (df["Atendimentos"] > 30).sum()
df["Atendimentos_Extras"] = df["Atendimentos"] - (3 * 10)
df["Atendimentos_Extras"] = df["Atendimentos_Extras"].apply(lambda x: x if x > 0 else 0)
df["Custo_Extra"] = df["Atendimentos_Extras"] * 1.0



def grafico_tendencia(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=df.index, y="Atendimentos", marker="o", linewidth=2)
    plt.axhline(y=30, color="red", linestyle="--", label="Capacidade Máxima (30)")

    plt.xlabel("Dias consecutivos")
    plt.ylabel("Número de Atendimentos")
    plt.title("Tendência de Atendimentos ao Longo do Tempo")
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_custos_extras(df):
    df_excedente = df[df["Custo_Extra"] > 0]

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_excedente, x="Data", y="Custo_Extra", color="red")

    plt.xlabel("Data")
    plt.ylabel("Custo Extra")
    plt.title("Custo Extra com Remuneração de Médicos")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    
grafico_tendencia(df)
grafico_custos_extras(df)
print(df_acima_30)
dias_excedidos = contar_dias_acima_30(df)
print(f"Número total de dias com atendimentos acima de 30: {dias_excedidos}")