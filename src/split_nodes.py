from textnode import TextNode, TextType
def split_nodes(old_nodes: list[TextNode], delimiter: str, text_type:TextType) -> TextNode:
    new_nodes = []
    for node in old_nodes:
        print(node.text)
        if node.text_type.name != "TEXT":
            new_nodes.append(node)
        node_split = node.text.split(delimiter)
        print(node_split)
        if len(node_split) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: {delimiter} closing is not found")
        nodes_to_add = [TextNode(node,TextType.TEXT) if i % 2 == 0 else TextNode(node, text_type) for i, node in enumerate(node_split)]
        print(nodes_to_add)
        new_nodes.extend(nodes_to_add)
        
    
    return new_nodes
