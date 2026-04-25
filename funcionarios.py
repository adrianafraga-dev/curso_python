import pandas as pd

df = pd.read_excel('dados_funcionarios.xlsx')

# Agrupar por Registro e nome
resultado = df.groupby(["Registro" , "Nome"])["Hora"].sum()

# Mostrando o Resultado

for (Registro, nome), hora in resultado.items():
    print(f"{Registro} - {nome} - {hora} hora")
