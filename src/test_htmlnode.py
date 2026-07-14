import unittest
from htmlnode import HTMLNode
class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        excepted = ' href="https://www.google.com" target="_blank"'
        htmlnode = HTMLNode("a", "Visit Google", "img", {
            "href":"https://www.google.com",
            "target":"_blank"
        })
        self.assertEqual(excepted, htmlnode.props_to_html())
    def test_fail_props(self):
        excepted = ' href="https://www.google.com"target="_blank"'
        htmlnode = HTMLNode("a", "Visit Google", "img", {
            "href":"https://www.google.com",
            "target":"_blank"
        })
        self.assertNotEqual(excepted, htmlnode.props_to_html())
    def test_single_prop(self):
        expected = ' class="container"'
        html_node = HTMLNode(
            "div",
            "Content",
            None,
            {
                "class": "container"
            }
        )

        self.assertEqual(expected, html_node.props_to_html())
    def test_empty_props(self):
        html_node = HTMLNode(
            "div",
            "Content",
            None,
            {}
        )

        self.assertEqual("", html_node.props_to_html())
if __name__ == "__main__":
    unittest.main()