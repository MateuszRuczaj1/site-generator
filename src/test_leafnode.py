import unittest
from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode('p',"This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode('a',"This is a link",{"href":"https://youtube.com/"})
        self.assertEqual(node.to_html(), '<a href="https://youtube.com/">This is a link</a>')

if __name__ == "__main__":
    unittest.main()