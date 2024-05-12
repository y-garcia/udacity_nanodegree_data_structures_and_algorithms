# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, segments, handler):
        node = self.root
        for segment in segments:
            node = node.insert(segment)
        node.handler = handler

    def find(self, segments):
        node = self.root
        for segment in segments:
            if node is None:
                return None
            node = node.children.get(segment)
        return node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, segment):
        return self.children.setdefault(segment, RouteTrieNode())


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.routeTrie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.routeTrie.insert(self.split_path(path), handler)

    def lookup(self, path):
        node = self.routeTrie.find(self.split_path(path))
        handler = None if node is None else node.handler
        return self.not_found_handler if handler is None else handler

    def split_path(self, path):
        if path is None or len(path) == 0 or path == '/':
            return []

        if path[-1] == '/':
            path = path[:-1]

        return path.split("/")


# Here are some test cases and expected outputs you can use to test your implementation
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

test_cases = [
    ("/", "root handler"),
    ("", "root handler"),
    (None, "root handler"),
    ("/home", "not found handler"),
    ("/home/", "not found handler"),
    ("/home/about", "about handler"),
    ("/home/about/", "about handler"),
    ("/home/about/me", "not found handler"),
]

for test_case in test_cases:
    input_value, expected = test_case
    result = router.lookup(input_value)
    print(f"router.lookup({input_value}) = '{result}' |",
          "Pass" if result == expected else f"Fail! '{expected}' expected")
