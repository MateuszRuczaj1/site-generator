import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_p_div(self):
        child_node = LeafNode("p","This is a children p tag",{"color":"red"})
        parent_node = ParentNode("div",[child_node], {"display":"flex"})
        self.assertEqual(parent_node.to_html(), '<div display="flex"><p color="red">This is a children p tag</p></div>')
    def test_to_html_multiple_children(self):
        child_node_1 = LeafNode("span", "This is a first child")
        child_node_2 = LeafNode("span", "This is a second child")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), "<div><span>This is a first child</span><span>This is a second child</span></div>")
    def test_to_html_none_children(self):
        self.assertRaises(ValueError, ParentNode("div", children=None).to_html)
    def test_to_html_with_nested(self):
        child_node = LeafNode("img", props={"src":"funny_photo.png", "alt":"Very funny cat", "width":"32", "height":"32"})
        parent_node = ParentNode("a",children=[child_node], props={"href":"/funny-images"})
        grandparent_node = ParentNode("div", children=[parent_node], props={"class":"image-wrapper"})
        self.assertEqual(grandparent_node.to_html(), '<div class="image-wrapper"><a href="/funny-images"><img src="funny_photo.png" alt="Very funny cat" width="32" height="32"></img></a></div>')
    if __name__ == "__main__":
        unittest.main()
