class HTMLNode():
    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("do the next lesson, maybe then!")
    
    def props_to_html(self):
        to_print = ""
        if not self.props:
            return ""
        for key in self.props:
            to_print += " " + key + "=" + '"' + self.props[key] + '"'
        return to_print

    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props={}):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        else:
            props_str = self.props_to_html()
            if self.tag == "img":
                return f"<{self.tag}{props_str} />"
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"