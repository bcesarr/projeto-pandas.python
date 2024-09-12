# Importando a biblioteca "Pandas" para trabalhar com arquvios "XLSX"
import pandas as pd

# Lendo a tabela .xlsx do excel.
tabela = pd.read_excel("tabela-teste-projeto-pandas.xlsx")

# Para vermos a tabela. - Para o Jupyter podemos usar display(tabela).
print(tabela)

# Localizando as celulas que queremos.Ex: tabela.loc[linha, coluna]
tabela.loc[tabela["Status"] == "Aumento", "Markups"] = 1.5  # Estamos pedindo para pegar todas as linhas em que o "Status" estiver como "Aumento", e mudar os "Markups" delas para 1.5.

# Fazendo o calculo entre os "Valores" base das frutas e os "Markups", para ter os "Novos Valores".
tabela["Novos Valores"] = tabela["Valores"] * tabela["Markups"]

print(tabela)

# Salvando a nova tabela (Se eu colocar o mesmo nome da tabela, ele substituirá automaticamente entre uma e outra).
# Para tirar o index (coluna com numeros na primeira coluna) que o Python coloca ao salvar a tabela, utilizamos "index=false".
tabela.to_excel("nova-tabela-teste-projeto-pandas.xlsx", index=False)