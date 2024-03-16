# tipos de texto inline
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

""" 
Classe que irá representar nós de texto inline 
PROPRIEDADES: 
    text - conteudo textual do nó 
    text_type: O tipo de texto que este nó contém (ex "bold", "italic", "link")
    url: url do link ou imagem, caso o texto seja um link 
"""
class TextNode:
    def __init__(self, text:str, text_type:str, url:str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # metodo que verifica se dois objetos TextNode são exatamente iguais    
    def __eq__(self, __value: object) -> bool:
        if (self.text == __value.text and
            self.text_type == __value.text_type and
            self.url == __value.url):
            return True
    
    # representação do objeto    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"