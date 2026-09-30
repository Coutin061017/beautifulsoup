import requests
from bs4 import BeautifulSoup

URL = "https://pt.wikipedia.org/"
HEADERS = {"User-Agent": "estudo-beautifulsoup/1.0"}


def buscar_pagina(url):
    resposta = requests.get(url, headers=HEADERS, timeout=10)
    resposta.raise_for_status()
    return resposta.text


def criar_soup(html):
    return BeautifulSoup(html, "html.parser")


def imprimir_h1(soup):
    h1 = soup.select_one("h1#firstHeading")
    if h1:
        print("H1:", h1.get_text(strip=True))
    else:
        print("Nenhum H1 encontrado")


def imprimir_link(soup):
    link = soup.find("a", href="https://pt.wikipedia.org/wiki/Chegou_a_Hora_de_Recomeçar")
    if link:
        print("Texto do link:", link.get_text(strip=True))
        print("Atributo href:", link["href"])
        print("Todos os atributos:", link.attrs)
    else:
        print("Nenhum link encontrado")


def main():
    html = buscar_pagina(URL)
    soup = criar_soup(html)
    imprimir_h1(soup)
    imprimir_link(soup)


if __name__ == "__main__":
    main()