import unittest

from blocktype import *

class TestBlockType(unittest.TestCase):

    def test_blocktype(self):
        test = """```
        this is code
        ```"""

        result = block_to_block_type(test)

        self.assertEqual(result, BlockType.CODE)

if __name__ == "__main__":
    unittest.main()