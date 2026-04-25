# Autor: Adriana Fraga
# projeto: Consumo de API
import requests

# variável que possui o CEP digitado pelo usuário 
cep = input('Digite seu CEP:')

# site com a API
url = f'https://viacep.com.br/ws/{cep}/json/'

# Método GET - exibe a informação
resposta = requests.get(url) 

# Tipo de arquivo da resposta
dados = resposta.json()

# condicional para erro  - cep não encontrado
if "erro" in dados:
    print('CEP não encontrado')
else:    
    print(f'Logradouro: {dados["logradouro"]}')
    print(f'Cidade: {dados["Cidade"]}')
    print(f'Estado: {dados["Estado"]}')
    print(f'Bairro: {dados["Bairro"]}')
