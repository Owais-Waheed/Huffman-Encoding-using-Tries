class RadixNode:
    def __init__(self, key=None, freq=None):
        self.key = key
        self.freq = freq
        self.children = {}
        self.isLeafNode = False

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def findPrefix(self, str1, str2):
        prefix = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i]!=str2[i]:
                break
            prefix += str1[i]
        return prefix

    def insert(self, key, freq):
        current_node = self.root
        while key:
            match = None
            for node_key, node_freq in current_node.children.items():
                if node_key.startswith(key[0]):
                    match = node_key
                    break
            if match:
                if key.startswith(match):
                    current_node = current_node.children[match]
                    key = key[len(match):]
                    if len(key) == 0:
                        current_node.isLeafNode = True
                else:
                    prefix = self.findPrefix(key, match)
                    current_node.children[prefix] = RadixNode(prefix, freq)
                    
                    new_node = current_node.children[prefix]

                    new_node.children[match[len(prefix):]] = RadixNode(match[len(prefix):], freq)
                    new_node.children[match[len(prefix):]].isLeafNode = True

                    if len(prefix) < len(key):
                        new_node.children[key[len(prefix):]] = RadixNode(key[len(prefix):], freq)
                        new_node.children[key[len(prefix):]].isLeafNode = True
                    else:
                        new_node.isLeafNode = True

                    del current_node.children[match]
                    return
            else:
                current_node.children[key] = RadixNode(key, freq)
                current_node.children[key].isLeafNode = True
                return

    def search(self, key):
        current_node = self.root
        while key:
            match = None
            for node_key, node_freq in current_node.children.items():
                if node_key.startswith(key[0]):
                    match = node_key
                    break
            if match:
                if key.startswith(match):
                    current_node = current_node.children[match]
                    key = key[len(match):]
                else:
                    return False
            else:
                return False
        if current_node.isLeafNode == True:
            return True
        else:
            print("xd")
            return False
    
# def main():
#     tree = RadixTree()

#     # insert the key-freq pair ("apple", 1)
#     tree.insert("water", 1)

#     # insert the key-freq pair ("application", 2)
#     tree.insert("slow", 2)

#     # insert the key-freq pair ("banana", 3)
#     tree.insert("slower", 3)

#     # insert the key-freq pair ("book", 4)
#     tree.insert("waste", 4)

#     # insert the key-freq pair ("booklet", 5)
#     tree.insert("watch", 5)

#     tree.insert("wa", 5)


#     print(tree.search("wa"))

# if __name__ == "__main__":
#     main()