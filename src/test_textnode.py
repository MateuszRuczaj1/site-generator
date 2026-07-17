import unittest
from textnode import TextNode, TextType, text_node_to_html
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node_2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is another text", TextType.BOLD)
        self.assertNotEqual(node, node_2)
    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.LINK)
        node_2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node_2)
    def test_not_eq_url(self):
        node = TextNode("This is a url", TextType.LINK, "https://google.com")
        node_2 = TextNode("This is a url", TextType.LINK)
        self.assertNotEqual(node, node_2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()