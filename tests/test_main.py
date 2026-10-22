"""Testes de extração de HTML sem acessar a internet."""

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import criar_soup, imprimir_link, imprimir_titulo, buscar_pagina


class ScrapingTests(unittest.TestCase):
    def test_extrai_titulo_e_link(self):
        html = '<html><head><title>Página de teste</title></head><body><main><a href="/produto">Produto</a></main></body></html>'
        saida = io.StringIO()
        with redirect_stdout(saida):
            soup = criar_soup(html)
            imprimir_titulo(soup)
            imprimir_link(soup)
        self.assertIn("Página de teste", saida.getvalue())
        self.assertIn("/produto", saida.getvalue())

    @patch("main.requests.get")
    def test_requisicao_usa_timeout(self, get):
        get.return_value.text = "<h1>OK</h1>"
        self.assertEqual(buscar_pagina("https://example.org"), "<h1>OK</h1>")
        self.assertEqual(get.call_args.kwargs["timeout"], 10)
        get.return_value.raise_for_status.assert_called_once()


if __name__ == "__main__":
    unittest.main()
