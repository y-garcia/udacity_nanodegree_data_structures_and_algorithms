# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        return self.children.setdefault(char, TrieNode())

    def suffixes(self, suffix='', result=None):
        # Recursive function that collects the suffix for
        # all complete words below this point
        if result is None:
            result = []

        if self.is_word and len(suffix) != 0:
            result.append(suffix)

        for char, node in self.children.items():
            node.suffixes(suffix + char, result)

        return result


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        if word is None:
            return

        node = self.root
        for char in word:
            node = node.insert(char)
        node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root

        if prefix is None:
            return node

        for char in prefix:
            if node is None:
                return None
            node = node.children.get(char)
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def print_suffixes(prefix):
    prefix_node = MyTrie.find(prefix)
    if prefix_node:
        print(f"'{prefix}' =>", prefix_node.suffixes())
    else:
        print(f"'{prefix}' not found")


prefixes = ['a', 'an', 'ant', 'f', 'fu', 'fun', 't', 'tr', 'tri', 'trie', 'x', '', None]

print("'prefix' => [suffixes]")
print("======================")
for prefix in prefixes:
    print_suffixes(prefix)
