from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0:
            raise ValueError("delimiter not closed, not valid markdown")
    
        parts = old_node.text.split(delimiter)

        split_nodes = []

        for i in range(len(parts)): 
            if i % 2 == 0:               
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

                    
                
def extract_markdown_images(text):
    alt_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_match

def extract_markdown_links(text):
    link_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_match

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
    
        tup = extract_markdown_images(old_node.text)

        if not tup:
            new_nodes.append(old_node)
            continue


        remaining_text = old_node.text

        for alt, url in tup:
            sections = remaining_text.split(f"![{alt}]({url})", maxsplit=1)
            if len(sections[0]) != 0: 
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
    
        tup = extract_markdown_links(old_node.text)

        if not tup:
            new_nodes.append(old_node)
            continue


        remaining_text = old_node.text

        for text, url in tup:
            sections = remaining_text.split(f"[{text}]({url})", maxsplit=1)
            if len(sections[0]) != 0: 
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            remaining_text = sections[1]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


    

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        if block:
            new_blocks.append(block.strip())
        
    return new_blocks


