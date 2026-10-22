"""Exemplo didático de extração de título e link com requests e BeautifulSoup."""

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


def imprimir_titulo(soup):
    titulo = soup.select_one("h1") or soup.title
    if titulo:
        print("Título:", titulo.get_text(strip=True))
    else:
        print("Nenhum título encontrado")


def imprimir_link(soup):
    # Usa um link real presente no HTML em vez de depender de um URL específico.
    link = soup.select_one("main a[href]") or soup.select_one("a[href]")
    if link:
        print("Texto do link:", link.get_text(strip=True))
        print("Atributo href:", link["href"])
    else:
        print("Nenhum link encontrado")


def main():
    try:
        html = buscar_pagina(URL)
    except requests.RequestException as erro:
        print(f"Não foi possível acessar a página: {erro}")
        return 1
    soup = criar_soup(html)
    imprimir_titulo(soup)
    imprimir_link(soup)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
