import unittest

from textnode import *



class TestTextNode(unittest.TestCase):
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD_TEXT)
    #     node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
    #     self.assertEqual(node, node2)
    
    # def invalid(self):
    #     node = TextNode("this will not work", TextType.INVALID, "HELLO.COM")
    #     node2 = TextNode("this will work", TextType.PLAIN_TEXT, "HELLO.COM")
    #     self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()