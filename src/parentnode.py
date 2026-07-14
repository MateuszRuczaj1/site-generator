from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        
        if not self.tag:
            raise ValueError("Parent node needs to have a tag")
        if not self.children:
            raise ValueError("Parent node needs to have a children")
        HTML_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            HTML_string += child.to_html()
        return HTML_string + f"</{self.tag}>"
    # def __repr__(self):
    #     return f"Tag: {self.tag}\nChildren: {self.children}\n"