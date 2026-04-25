from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Configuração do navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.implicitly_wait(10)

# Acessa o site
navegador.get("https://books.toscrape.com")

print("Pegando os dados...")

# Lista dos livros
livros = navegador.find_elements(By.CSS_SELECTOR, "article.product_pod")

# Pegando apenas os 2 primeiros
for livro in livros[:2]:
    nome = livro.find_element(By.TAG_NAME, "h3").text
    preco = livro.find_element(By.CLASS_NAME, "price_color").text
    
    print("Livro:", nome)
    print("Preço:", preco)
    print("-" * 30)

navegador.quit()