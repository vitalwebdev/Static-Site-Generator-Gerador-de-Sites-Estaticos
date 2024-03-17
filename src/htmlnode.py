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
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


"""
Classe para representar tags HTML sem filhos (nivel mais baixo da DOM)
PROPRIEDADES:
    tag - string que representa a tag HTML (ex p, a, h1, etc)
    value - string que representa o valor da tag HTML (ex o texto dentro do paragrafo) OBRIGATORIO
    props - dicionario representando os atributos da tag HTML, formato {"atributo": "valor"}
"""    
class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict = None):
        super().__init__(tag, value, None, props)
        
        def to_html(self):
            if self.value is None:
                raise ValueError("Invalid HTML: no value")
            if self.tag is None:
                return self.value
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
        