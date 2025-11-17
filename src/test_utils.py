import unittest
from utils import extract_markdown_images, extract_markdown_links, markdown_to_blocks, markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links."
        result = extract_markdown_links(text)
        self.assertEqual(result, [])
    
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])

    def test_markdown_to_blocks_with_empty_lines(self):
        markdown = """# Heading


This is a paragraph.


* List item 1
* List item 2"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# Heading",
            "This is a paragraph.",
            "* List item 1\n* List item 2"
        ])

    def test_markdown_to_blocks_no_blocks(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [])

class TestMarkdownToHTMLNode(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

