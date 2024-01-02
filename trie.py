class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None
        
    def is_leaf(self):
        """
        Returns True if the node is a leaf node (i.e., has no children), False otherwise.
        """
        return self.left is None and self.right is None

    def get_chars(self):
        """
        Returns the set of characters represented by the node.
        """
        return {self.char} if self.char is not None else set()

    def get_code(self):
        """
        Returns the Huffman code for the node.
        """
        return ''

class HuffmanTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, code, char):
        node = self.root
        for bit in code:
            if bit == '0':
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right
        node.char = char

    def search(self, node, char):
        """
        Searches the Huffman trie for the given character and returns its Huffman code.

        :param node: The current node to search from.
        :param char: The character to search for.
        :return: The Huffman code for the character, or None if it is not in the trie.
        """
        
        if node is None:
            return None

        if node.is_leaf() and char in node.get_chars():
            return node.get_code()

        left_result = self.search(node.left, char)
        if left_result is not None:
            return '0' + left_result

        right_result = self.search(node.right, char)
        if right_result is not None:
            return '1' + right_result

        return None


'''
    def search(self, code):
        node = self.root
        for bit in code:
            if bit == '0':
                node = node.left
            else:
                node = node.right
        return node.char
'''