from textnode import TextNode, TextType
def split_nodes(old_nodes: list[TextNode], delimiter: str, text_type:TextType) -> TextNode:
    new_nodes = []
    for node in old_nodes:
       
        if node.text_type.name != "TEXT":
            new_nodes.append(node)
            continue
        node_split = node.text.split(delimiter)
        if len(node_split) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: {delimiter} closing is not found")
        nodes_to_add = []
        for i, text in enumerate(node_split):
            if text=="":
                continue
            if i % 2 == 0:
                nodes_to_add.append(TextNode(text, TextType.TEXT))
            else:
                nodes_to_add.append(TextNode(text, text_type))

        
        new_nodes.extend(nodes_to_add)
        
    
    return new_nodes
