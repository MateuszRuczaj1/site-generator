from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    TEXT="text"
    BOLD="bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        is_equal = False
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            is_equal = True
        return is_equal
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b",value=text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i",value=text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", value=text_node.text)
        case TextType.LINK:
            return LeafNode("a", value=text_node.text, props={"href":text_node.url})
        