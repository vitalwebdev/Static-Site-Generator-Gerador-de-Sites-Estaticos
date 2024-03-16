import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    
    # Este teste cria dois objetos TextNode com as mesmas propriedades e verifica se são iguais.
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    # Este teste cria dois objetos TextNode com tipos diferentes e verifica se são diferentes.
    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    # Este teste cria dois objetos TextNode com tipos iguais e conteúdos diferentes, e verifica se são diferentes.
    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    # # Este teste cria dois objetos TextNode com urls e verifica se são iguais.
    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        self.assertEqual(node, node2)

    # Teste da represetação textual do objeto (método repr)
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
