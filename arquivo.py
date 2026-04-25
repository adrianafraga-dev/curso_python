# Escrever em arquivos

'''
Comando ara ler e Escrever Arquivos 

with open(file = "caminho do arquivo", mode='Modo de leitura ou Escrita', encoding=' decodificado') as apelido:
    bloco de código
'''

'''
O Modo de Escrita - W
O modo de Leitura - R
O Modo de Acréscimo - A
'''
nome_do_arquivo = "pepsico.txt"
with open(file =nome_do_arquivo,   mode="w", encoding= 'utf8') as arquivo:
    print(f'''Em 1992 nas filipinas, ocorreu o Incidente 349 uma promoção da empresa Pepsi,
 se tornou um desantre. Tampinhas premiadas com números diários, resultariam em um grande premio,
 Em 25 maio, o numero 349 foi anunciado como vencedor, mas um erro de programação fez com que inumeras
 tampinhas tivesse esse numero''', file=arquivo)