from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None,props = None):
        super().__init__(tag, value, props=props)
    def to_html(self):
        HTML_string = ""
        if not self.value:
            raise ValueError
        if not self.tag:
            HTML_string=self.value
        else:
            HTML_string=f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return HTML_string
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps: {self.props_to_html()}"
    