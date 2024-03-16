"""
Classe para representar nós HTML da DOM
PROPRIEDADES:
    tag - string que representa a tag HTML (ex p, a, h1, etc)
    value - string que representa o valor da tag HTML (ex o texto dentro do paragrafo)
    children - lista de objetos HTMLNode filhos deste nó
    props - dicionario representando os atributos da tag HTML, formato {"atributo": "valor"}
"""
class HTMLNode:
    def __init__(self, 
                 tag:str = None, 
                 value:str = None, 
                 children:list = None, 
                 props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attr_list = [" "]
        for key, value in self.props.items():
            attr_list.append(f"{key}='{value}'")
            
        return " ".join(attr_list)
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
        