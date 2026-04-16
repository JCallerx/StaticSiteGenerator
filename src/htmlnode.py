class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("error")
    
    def props_to_html(self):

        if self.props is None or len(self.props) == 0 :
            return ""

        formatted = ""

        for key, value in self.props.items():
            formatted += f' {key}="{value}"'
        return formatted
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        inner = ""
        if self.tag is None:
            raise ValueError("Tag is missing")
        
        if self.children is None:
            raise ValueError("child is required")
        
        for child in self.children:
            inner += child.to_html()


        return f'<{self.tag}{super().props_to_html()}>{inner}</{self.tag}>'
        
    
    