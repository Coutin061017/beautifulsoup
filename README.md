# Scraping da Wikipédia com BeautifulSoup

Projeto de estudo em Python que acessa a página inicial da [Wikipédia em português](https://pt.wikipedia.org/), baixa o HTML com `requests` e usa o `BeautifulSoup` para extrair informações da página.

## O que o projeto faz

- Faz uma requisição `GET` à Wikipédia
- Passa o conteúdo da página (`resposta.text`) para o BeautifulSoup
- Exibe o primeiro `<h1>` encontrado ou o título `<title>` como alternativa.
- Exibe um link presente no HTML, seu texto e o atributo `href`.
- Mostra uma mensagem de erro caso a requisição HTTP falhe.

## Como funciona

```
URL -> requests (busca a página) -> HTML -> BeautifulSoup (lê o HTML) -> dados
```

O `requests` acessa a internet e traz a página. O BeautifulSoup não acessa nada: ele só lê o HTML que já foi baixado.

## Tecnologias

- Python
- requests
- beautifulsoup4
- Jupyter Notebook
- Git e GitHub

## Arquivos

```
beautifulsoup/
├── main.py            # código principal, separado em funções
├── main.ipynb         # notebook para testar passo a passo
├── requirements.txt   # bibliotecas do projeto
└── README.md
```

## Como rodar

1. Clone o projeto:

```bash
git clone https://github.com/Coutin061017/beautifulsoup.git
cd beautifulsoup
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux/Mac, use `source .venv/bin/activate` para ativar.

3. Instale as bibliotecas:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python main.py
```

Para testar no notebook, rode `jupyter notebook` e abra o `main.ipynb`. Se estiver no VS Code, escolha o Python da pasta `.venv` como kernel.

## Testes

Os testes usam HTML fictício e não precisam acessar a Wikipédia:

```powershell
python -m unittest discover -s tests -v
```

## O que eu aprendi

- Como usar o `requests` para buscar uma página, com `headers`, `timeout` e `raise_for_status()`
- A diferença entre `find()` (devolve `None` se não achar) e `find_all()` (devolve uma lista)
- Como pegar atributos de uma tag, como o `href`
- Como criar um ambiente virtual e por que o `requirements.txt` existe
- Como versionar o projeto com Git e enviar para o GitHub


## Autor

André Coutinho - [GitHub](https://github.com/Coutin061017)
