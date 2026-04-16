import unittest

from htmlnode import *


# class TestHTMLNode(unittest.TestCase):
    # def test_props_to_html_single(self):
    #     node = HTMLNode("h1", "hello world", [], {"role": "heading"} )
    #     result = node.props_to_html()
    #     self.assertEqual(result, ' role="heading" ')

    # def test_props_to_html_multiple(self):
    #     node = HTMLNode("h1", "hello world", [], {"role": "heading", "aria-hidden": "true"} )
    #     result = node.props_to_html()
    #     self.assertEqual(result, ' role="heading" aria-hidden="true" ')

    # def test_props_to_html_none(self):
    #     node = HTMLNode("h1", "hello world", [], None )
    #     result = node.props_to_html()
    #     self.assertEqual(result, ''), 

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_one_prop(self):
        node = LeafNode("p", "Hello, world!", {"aria-hidden": "true"})
        self.assertEqual(node.to_html(), '<p aria-hidden="true">Hello, world!</p>')

    def test_leaf_to_html_many_props(self):
        node = LeafNode("p", "Hello, world!", {"aria-hidden": "true", "id": "4", "class": "header"})
        self.assertEqual(node.to_html(), '<p aria-hidden="true" id="4" class="header">Hello, world!</p>')

    
if __name__ == "__main__":
    unittest.main()