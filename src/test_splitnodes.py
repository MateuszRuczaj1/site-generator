import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes
class TestSplitNodes(unittest.TestCase):
    def test_spilt_nodes_with_code(self):
        expected = [
        TextNode("String ",TextType.TEXT,None),
        TextNode("Code", TextType.CODE_TEXT,None),
        TextNode(" String", TextType.TEXT,None)
        ]
        node = TextNode("String `Code` String", TextType.TEXT)
        actual = split_nodes([node], "`", TextType.CODE_TEXT)
        self.assertEqual(expected, actual)
    def test_split_nodes_with_bold(self):
        expected = [
        TextNode("Regular text part 1 ",TextType.TEXT,None),
        TextNode("BOLD!!!", TextType.BOLD,None),
        TextNode(" Regular text part 2", TextType.TEXT,None)
        ]
        node = TextNode("Regular text part 1 **BOLD!!!** Regular text part 2", TextType.TEXT)
        actual = split_nodes([node], "**", TextType.BOLD)
        self.assertEqual(expected, actual)
    def test_split_nodes_with_italic(self):
        expected = [
            TextNode("Lorem ipsum ", TextType.TEXT, None),
            TextNode("dolor", TextType.ITALIC_TEXT, None),
            TextNode(" sit amet", TextType.TEXT, None)
        ]
        node = TextNode("Lorem ipsum _dolor_ sit amet", TextType.TEXT)
        actual = split_nodes([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(expected, actual)
    
    def test_split_multiple_nodes_with_italic(self):
        expected = [
            TextNode("Lorem ipsum ", TextType.TEXT, None),
            TextNode("dolor", TextType.ITALIC_TEXT, None),
            TextNode(" sit amet, ", TextType.TEXT, None),
            TextNode("consectetur", TextType.ITALIC_TEXT, None),
            TextNode(" adipiscing elit.", TextType.TEXT, None)
        ]
        node = TextNode("Lorem ipsum _dolor_ sit amet, ", TextType.TEXT)
        node_2 = TextNode("_consectetur_ adipiscing elit.", TextType.TEXT)
        actual = split_nodes([node, node_2], "_", TextType.ITALIC_TEXT)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
