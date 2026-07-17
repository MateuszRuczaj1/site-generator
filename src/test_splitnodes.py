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

if __name__ == "__main__":
    unittest.main()
