class HTMLNode():
    def __init__(self, tag = None, value=None, children=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props:
            string = " "
            for key, value in self.props.items():
                string+=f'{key}="{value}" '
            return string
        else:
            return ""
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props_to_html()}"
    