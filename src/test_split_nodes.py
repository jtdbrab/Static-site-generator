import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_split_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ])

    def test_split_italic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL),
        ])

    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])