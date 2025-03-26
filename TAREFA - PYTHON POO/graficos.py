import pandas as pd # permite ler, manipular e escrever tabelas do Excel de forma eficiente usando DataFrames.
import matplotlib.pyplot as plt #permite criar gráficos e visualizações de dados de forma simples e intuitiva, Matplotlib é essencial para personalizações avançadas.
import seaborn as sns #  cria gráficos, facilita e deixa tudo mais bonito com menos código. Simplifica a visualização quando se trabalha com DataFrames
                      # seaborn estende de matplotlib 

df = pd.read_excel('consultas.xlsx')

# VARIAVEL padrao_diario_consultas USADA PARA OS DOIS ÚLTIMOS GRÁFICOS
quantidadeDeMedicos = 3
contratoMedicosConsultas = 10
padraoConsultaPorDia = quantidadeDeMedicos * contratoMedicosConsultas


#===============CONSULTAS MENSAIS=======================
totalMes = 0
dadosMensal = []
meses = ["Janeiro", "Fevereiro", "Março"] # para colocar no eixo do gráfico

def dadosGraficoMensal(coluna):
  global totalMes
  if coluna in [4, 8, 12]:
    dadosMensal.append(totalMes)
    totalMes = 0

for coluna in range(12):
  for linha in range(5):
    totalMes += df.iloc[linha + 2, coluna + 1]
  dadosGraficoMensal(coluna + 1) 

#DataFrame para o gráfico Mensal
df_grafico_mensal = pd.DataFrame({
  "Mês": meses,
  "Consultas": dadosMensal
}) 

# Gráfico: Consultas Mensais e suas configurações 
plt.figure(figsize=(10,5))
sns.lineplot(data=df_grafico_mensal, x="Mês", y="Consultas", marker="o", label="Consultas Mensais")
plt.title("Número de Consultas por Mês")
plt.xlabel("Mês")
plt.ylabel("Total de Consultas")
plt.legend()
plt.grid()
plt.show() #Exibir o gráfico


#============CONSULTAS SEMANAIS===============

totalSemanal = 0
dadosSemanal = []
semanas = ["sem 1","sem 2","sem 3","sem 4","sem 5","sem 6","sem 7","sem 8","sem 9","sem 10","sem 11","sem 12"]
#variavel semanas usada para os graficos de qtd de consultas semanais e custo de consultas extras semanais

for coluna in range(12):
  for linha in range(5):
    totalSemanal += df.iloc[linha + 2, coluna + 1]

  dadosSemanal.append(totalSemanal)
  totalSemanal = 0 # zera a variavel para reiniciar a nova contagem da proxima semana

#DataFrame para o gráfico Semanal
df_grafico_semanal = pd.DataFrame({
  "Semana": semanas,
  "Consultas": dadosSemanal
})
 
# Gráfico: Consultas Semanais e suas configurações 
plt.figure(figsize=(10, 5)) # altura 10 , largura 5
sns.lineplot(data=df_grafico_semanal, x="Semana", y="Consultas", marker="o", label="Consultas Semanais")
plt.title("Número de Consultas por Semana")
plt.xlabel("Semana")
plt.ylabel("Total de Consultas")
plt.legend()
plt.grid()
plt.show()


#=================CUSTO POR SEMANA=================
valorConsulta = 200 # variavel sera usada para esse grafico de custo por semana e para o grafico custo por mes
valorTotalSemana = 0 
custoMedicosSemanal = []
 
for coluna in range(12):
  for linha in range(5):
    consultaSemana = df.iloc[linha + 2, coluna + 1]
    if consultaSemana > padraoConsultaPorDia:
      consultasExtras = consultaSemana - padraoConsultaPorDia
      valorTotalSemana += (consultasExtras * valorConsulta) * 2

  custoMedicosSemanal.append(valorTotalSemana)
  valorTotalSemana = 0

# DataFrame para o gráfico de Custo para consultas extras semanais 
df_grafico_custo_semanal = pd.DataFrame({
    "Semana": semanas,
    "Consultas Extras": custoMedicosSemanal,
})

# Gráfico: Consultas extras Semanais e suas configurações
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_grafico_custo_semanal, x="Semana", y="Consultas Extras", marker="s", color="red", label="Custo Semanal")
plt.title("Custo das Consultas Extras por Semana")
plt.xlabel("Semana")
plt.ylabel("Custo por Semana")
plt.legend()
plt.grid()
plt.show()

# =================QUANTIDADE DE CONSULTAS EXTRAS POR SEMANA=================
consultasExcedentesDiarias = []  # Lista para armazenar os excessos diários por semana

for coluna in range(12):
    semana_excedentes = []  # Lista para armazenar os excessos diários dessa semana

    for linha in range(5):
        consultaSemana = df.iloc[linha + 2, coluna + 1]
        if consultaSemana > padraoConsultaPorDia:
            excedente = consultaSemana - padraoConsultaPorDia
        else:
            excedente = 0  # Se não exceder, o valor é 0

        semana_excedentes.append(excedente)  # Adiciona o valor do dia à lista da semana

    consultasExcedentesDiarias.append(semana_excedentes)

# Criar DataFrame com os dados organizados
dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex"]
semanas = [f"Semana {i}" for i in range(1, 13)]
df_excedentes = pd.DataFrame(consultasExcedentesDiarias, columns=dias_da_semana, index=semanas)

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Criar heatmap com seaborn
sns.heatmap(df_excedentes, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".0f")

# Configurações do gráfico
plt.title("Excedente de Consultas por Dia e Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Semana")

# Exibir o gráfico
plt.show()

#====================CUSTO POR MÊS=======================
valorTotalMes = 0 
custoMedicosMensal = []

def dadosGraficoCustoMensal(coluna):
  global valorTotalMes
  if coluna in [4, 8, 12]:
    print(valorTotalMes)
    custoMedicosMensal.append(valorTotalMes)
    valorTotalMes = 0


for coluna in range(12):
  for linha in range(5):
    consultaMes = df.iloc[linha + 2, coluna + 1]
    if consultaMes > padraoConsultaPorDia:
      consultasExtras = consultaMes - padraoConsultaPorDia
      valorTotalMes += (consultasExtras * valorConsulta) * 2
  dadosGraficoCustoMensal(coluna + 1)   

# # DataFrame para o gráfico de Custo para consultas extras mensais
df_grafico_custo_mensal = pd.DataFrame({
    "Mês": meses,
    "Custo Extra Consultas Mensal": custoMedicosMensal,
})

# # Gráfico: Custo  mensais e suas configurações
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_grafico_custo_mensal, x="Mês", y="Custo Extra Consultas Mensal", marker="s", color="red", label="Custo Mensal")
plt.title("Custo das Consultas extras por Mês")
plt.xlabel("Mês")
plt.ylabel("Custo por Mês")
plt.legend()
plt.grid()
plt.show()

 




