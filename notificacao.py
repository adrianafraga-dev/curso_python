import requests

nome = (input("Digite seu nome"))

topico = "Adriana"

url = f"https://ntfy.sh/{topico}"

mensagem = f"O {nome} acabou de te mandar um salve"

requests.post(url, data = "Olá Mundo!, Meu primeiro alerta feito por Adriana".encode('utf-8'))


print(f"Salve enviado para {topico}!")  