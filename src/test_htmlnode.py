import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode("h1", "hello world", [], {"role": "heading"} )
        result = node.props_to_html()
        self.assertEqual(result, ' role="heading" ')

    def test_props_to_html_multiple(self):
        node = HTMLNode("h1", "hello world", [], {"role": "heading", "aria-hidden": "true"} )
        result = node.props_to_html()
        self.assertEqual(result, ' role="heading" aria-hidden="true" ')

    def test_props_to_html_none(self):
        node = HTMLNode("h1", "hello world", [], None )
        result = node.props_to_html()
        self.assertEqual(result, ''), 


    
if __name__ == "__main__":
    unittest.main()