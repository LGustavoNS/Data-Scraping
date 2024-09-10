import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cotacao+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

#No headers acima, estamos passando um dicionario Python para ele poder identificar a buscar, assim passando um filtro mais limpo para a nossa requisição.

requisicao = requests.get(link, headers=headers)
print(requisicao)

#print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")

# print(site.prettify()) # Essa função serve para poder organizar o código do HTML, ou seja, ele está indentando meu código e o deixando mais legivel

# print (site.title) #Eu estou fazendo um print para ele poder me retornar o titulo do site

#titulo = site.find("title")
#print(titulo)

# Desse modo acima, estamos tentando fazer uma pesquina para encontrar o Title do link do site.

"""
pesquisa = site.find_all("input")
print(pesquisa[1])

# Desse modo acima, estamos tentando fazer uma pesquina para encontrar o Input do link do site.
"""

# Desse modo abaixo, estamos tentando fazer uma pesquina pelo input a class correspondente ao link do site para retornar algo.
#pesquisa2 = site.find("input", class_="gLFyf")
#print(pesquisa2)

#print(pesquisa2["value"]) #Desse modo acima, estamos tentando fazer uma pesquina pelo atributo dele, no caso o Value.

cotacao_dolar = site.find("span", class_="SwHCTb")
print(cotacao_dolar.get_text()) #Dessa forma, eu posso obter o resultado que está dentro do atributo text
print(cotacao_dolar["data-value"]) # Dessa forma eu posso obter o resultado que está dentro do atributo do data-value