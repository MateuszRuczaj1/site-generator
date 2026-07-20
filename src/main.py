from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes import split_nodes
from extract_links_and_images import extract_markdown_images, extract_markdown_links
def main():
    text = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    html_node = HTMLNode("h1", "This is main header", "p", {
        "color":"red",
        "href": "https://google.com/"
    })
    leaf_node = LeafNode("p","This is a paragraph")
    # print(text)
    # print(html_node)
    # print(leaf_node.to_html())
    # print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
    child_node = LeafNode("span","child")
    parent_node = ParentNode("div",[child_node])
    # print(parent_node.to_html())
    node = TextNode("Lorem ipsum _dolor_ sit amet,", TextType.TEXT)
    node_2 = TextNode("consectetur adipiscing elit.", TextType.TEXT)
    print(split_nodes([node,node_2], "_", TextType.ITALIC_TEXT))
    print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
    
main()