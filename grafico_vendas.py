"""
Com vendas oscilando de mês em mês, uma emoresa buscou clareza para planejar melhor suas metas
e controle de estoque. Utilizando modelos de séries temporais, criamos uma previsão que revela padrões
de crescimento e sazonalidade. O time comercial agora sabe com antecedência os meses mais fracos e mais fortes,
ajustando estratégias e evitando tanto rupturas quanto excesso de estoque.
"""
import pandas as pd
import matplotlib.pyplot as plt 

vendas = pd.DataFrame({
    "Data": pd.date_range(start='2024-01-01', periods=24, freq='ME'),
    "Vendas": [1000, 1150, 980, 1300, 1100, 1250, 900, 1400, 1350, 1200, 1700, 1500,
               1600, 1800, 1550, 2000, 1700, 1650, 1900, 2100, 1950, 2200, 2050, 2300 ] 
})
vendas["Media_Movel"] = vendas["Vendas"].rolling(window=3).mean() # pego todos os dados e faço uma média

# Grafico

plt.figure(figsize=(10,5)) # proporções do grafico
plt.plot(vendas["Data"], vendas["Vendas"], label="Vendas", marker="o") # vendas reais
plt.plot(vendas["Data"], vendas["Media_Movel"], label= "Media_Movel (3 meses)", linestyle="--") ## ocilação de crescimento ou queda
plt.title("Evolução das Vendas com Média Móvel") # titulo do gráfico
plt.xlabel("Data") # eixo x
plt.ylabel("Valor das Vendas") # eixo y
plt.legend() # legenda do gráfico
plt.grid(True) # grade ligada
plt.tight_layout() # layout
plt.show() # mostrar o gráfico