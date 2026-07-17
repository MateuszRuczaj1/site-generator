from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes import split_nodes
def main():
    text = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    html_node = HTMLNode("h1", "This is main header", "p", {
        "color":"red",
        "href": "https://google.com/"
    })
    leaf_node = LeafNode("p","This is a paragraph")
    print(text)
    print(html_node)
    print(leaf_node.to_html())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
    child_node = LeafNode("span","child")
    parent_node = ParentNode("div",[child_node])
    print(parent_node.to_html())
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes([node], "`", TextType.CODE_TEXT)
main()