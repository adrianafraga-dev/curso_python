# Autor Adriana Fraga

# Fazer uma função que indica que o numero é par

numero = int (input('Digite o número:'))

def ehpar(var):
  print(' O numero digitado é par? \n' , var % 2 == 0)


  if numero % 2 == 0:

         print ('É par!')

  else:
      print ('É Impar!')

ehpar(numero)







