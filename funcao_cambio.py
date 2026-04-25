# Autor Adriana Fraga
# Função Python
# Função transformar real em dólar

real= float(input('Digite o valor:'))
dolar= float(input('Digite o valor:'))


#funcao para converter real para dolar 
def converter_real_para_dolar(dolar, real): 
   conversao = real/dolar

   print(f' O Valor convertido em U$: {conversao:.2f}')
   return conversao

# chamando a função

def linha (): 
    texto = input (' Insira o simbolo para linha')
    print (texto * 50)

linha()
converter_real_para_dolar (dolar,real)

linha ()
for i in range (11):
   linha ()


