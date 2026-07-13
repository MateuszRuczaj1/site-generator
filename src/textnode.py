from enum import Enum
class TextType(Enum):
    TEXT="text"
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
    
