import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

class TestSplitNodesImage(unittest.TestCase):
    def test_split_image(self):
        node = TextNode("This is text with an image ![alt text](https://example.com/image.png)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        ])

    def test_split_multiple_images(self):
        node = TextNode("Image one ![one](https://example.com/one.png) and image two ![two](https://example.com/two.png)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("Image one ", TextType.NORMAL),
            TextNode("one", TextType.IMAGE, "https://example.com/one.png"),
            TextNode(" and image two ", TextType.NORMAL),
            TextNode("two", TextType.IMAGE, "https://example.com/two.png")
        ])

    def test_no_images(self):
        node = TextNode("This is text with no images.", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

class TestSplitNodesLink(unittest.TestCase):
    def test_split_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ])

    def test_split_multiple_links(self):
        node = TextNode("Link one [one](https://example.com/one) and link two [two](https://example.com/two)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("Link one ", TextType.NORMAL),
            TextNode("one", TextType.LINK, "https://example.com/one"),
            TextNode(" and link two ", TextType.NORMAL),
            TextNode("two", TextType.LINK, "https://example.com/two")
        ])

    def test_no_links(self):
        node = TextNode("This is text with no links.", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_text_to_textnodes_no_formatting(self):
        text = "This is plain text with no formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode(text, TextType.NORMAL)])

    def test_text_to_textnodes_only_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL),
        ])

    def test_text_to_textnodes_only_italic(self):
        text = "This is *italic* text."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.NORMAL),
        ])

    def test_text_to_textnodes_only_code(self):
        text = "This is `code` text."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.NORMAL),
        ])

    def test_text_to_textnodes_only_image(self):
        text = "This is an image ![alt text](https://example.com/image.png)."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is an image ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.NORMAL),
        ])

    def test_text_to_textnodes_only_link(self):
        text = "This is a link [to boot dev](https://www.boot.dev)."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(".", TextType.NORMAL),
        ])