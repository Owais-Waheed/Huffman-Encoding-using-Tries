from queue import PriorityQueue
from trie import *

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    freq_table = {}
    for char in text:
        freq_table[char] = freq_table.get(char, 0) + 1
    return freq_table

#This function constructs Huffman Tree

def build_huffman_tree(freq_table):
    pq = PriorityQueue()
    for char, freq in freq_table.items():
        pq.put(Node(freq, char))
    
    while pq.qsize() > 1:
        node1 = pq.get()
        node2 = pq.get()
        parent = Node(node1.freq + node2.freq, left=node1, right=node2)
        pq.put(parent)
    
    return pq.get()

#This function constructs Huffman Trie

def build_huffman_codes(node, prefix='', huffmanTrie=HuffmanTrie()):
    if node.char:
        huffmanTrie.insert(prefix, node.char)
    else:
        build_huffman_codes(node.left, prefix + '0', huffmanTrie)
        build_huffman_codes(node.right, prefix + '1', huffmanTrie)
    return huffmanTrie

def compress(text):
    freq_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(freq_table)
    huffmanTrie = build_huffman_codes(huffman_tree)

    # encoded_text = ''.join([huffmanTrie.search(char) for char in text])
    encoded_text = ''
    for char in text:
        encoded_text+= huffmanTrie.search(huffmanTrie.root, char)

    return (freq_table, encoded_text)

def decompress(freq_table, encoded_text):
    huffman_tree = build_huffman_tree(freq_table)
    decoded_text = ''
    node = huffman_tree
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            decoded_text += node.char
            node = huffman_tree
    return decoded_text
'''
# Example usage
text = "hello world"
freq_table, encoded_text = compress(text)
decoded_text = decompress(freq_table, encoded_text)
print(f"Original text: {text}")
print(f"Compressed text: {encoded_text}")
print(f"Decoded text: {decoded_text}")
'''