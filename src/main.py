from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
def main():
    text = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    html_node = HTMLNode("h1", "This is main header", "p", {
        "color":"red",
        "href": "https://google.com/"
    })
    print(text)
    print(html_node)
main()