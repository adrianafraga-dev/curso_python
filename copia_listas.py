# Autor: Adriana Fraga 
# Projeto: Cópia de Listas

# Em Python as listas são um recurso muito poderoso mas todo poder 
# trás responsabilidades vamos ver um çefeito colateral ao copiar 
# uma lista

L = [1, 2, 3, 4, 5]

V = L 

print ('Essa  é a lista L: ' , L)
print ('Essa  é a lista V: ' , V)


V[0] = 6 
print ('Essa é a lista V modificada:', V)
print ('Essa é a lista L modificada:', L)

L = [1, 2, 3, 4, 5]
V = L [:]
V  [0] = 6

print ('Essa  é a lista L: ' , L)
print ('Essa  é a lista V: ' , V)


