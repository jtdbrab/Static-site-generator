import unittest
from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode: a, Click here, [], {'href': 'https://www.google.com'}")

    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(repr(node), 'HTMLNode: None, None, [], {}')

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("i", "italic text"),
            ],
        )
        self.assertEqual(node.to_html(), "<div><p><b>Bold text</b>Normal text</p><i>italic text</i></div>")

    def test_value_error_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_value_error_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)
