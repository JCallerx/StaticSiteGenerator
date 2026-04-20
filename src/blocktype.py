from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(md_block):
    header = re.findall(r'^#+ ', md_block)
    code = re.findall(r"```\n[\s\S]*?```", md_block)
    quote = re.findall(r"^>\s?", md_block)
    unordered = re.findall(r"^- ", md_block)
    ordered = re.findall(r"(?<!\S)\d{1,2}\.\s((?:(?!,\s\d{1,2}\.).)+)", md_block)


    if header:
        return BlockType.HEADING
    elif code:
        return BlockType.CODE
    elif quote:
        return BlockType.QUOTE
    elif unordered:
        return BlockType.UNORDERED_LIST
    elif ordered:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH