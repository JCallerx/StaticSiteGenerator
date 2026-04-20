from helpers import *
from blocktype import *
import re



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    return children


def heading_to_html_node(text):
    match = re.match(r"#{1,6} ", text)
    count = len(match.group()) - 1
    cleaned = text[len(match.group()):]
    children = text_to_children(cleaned)
    node = ParentNode(f"h{count}", children)
    return node

def quote_to_html_node(text):
    arr = text.split("\n")
    new_arr = []
    for line in arr:
        new_arr.append(re.sub(r"^>\s?", "", line))
    new = " ".join(new_arr)
    children = text_to_children(new)
    return ParentNode("blockquote", children)

def paragraph_to_html_node(text):
    new_text = text.replace("\n", " ")
    children = text_to_children(new_text)
    return ParentNode("p", children)

def UL_to_html_node(text):
    block = text.split("\n")
    li_items = []
    for i in block:
        stripped = re.sub(r"^- ", "", i)
        children = text_to_children(stripped)
        li_items.append(ParentNode("li", children))
    return ParentNode("ul", li_items)

def OL_to_html_node(text):
    block = text.split("\n")
    li_items = []
    for i in block:
        stripped = re.sub(r"^\d+\.\s", "", i)
        children = text_to_children(stripped)
        li_items.append(ParentNode("li", children))
    return ParentNode("ol", li_items)

def code_to_html_node(text):
    cleaned = text[4:-3]
    node = TextNode(cleaned, TextType.TEXT)
    child = text_node_to_html_node(node)
    temp = ParentNode("code", [child])
    return ParentNode("pre", [temp])



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is BlockType.PARAGRAPH:
            node = paragraph_to_html_node(block)
            node_list.append(node)
        elif block_type is BlockType.HEADING: 
            node = heading_to_html_node(block)
            node_list.append(node)
        elif block_type is BlockType.QUOTE:
            node = quote_to_html_node(block)
            node_list.append(node)
        elif block_type is BlockType.UNORDERED_LIST:
            node = UL_to_html_node(block)
            node_list.append(node)
        elif block_type is BlockType.ORDERED_LIST:
            node = OL_to_html_node(block)
            node_list.append(node)
        else:
            node = code_to_html_node(block)
            node_list.append(node)
    div = ParentNode("div", node_list)

    return div


    

        
