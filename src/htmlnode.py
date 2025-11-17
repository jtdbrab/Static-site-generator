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