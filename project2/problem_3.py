import sys
from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.char}, {self.frequency})"


class MinHeap:
    def __init__(self, nodes=None):
        self.heap = None
        self.heapify(nodes)

    def insert(self, node):
        self.heap.append(node)

        index = len(self.heap) - 1
        while index > 0:
            parent_index = self.get_parent(index)

            if self.heap[parent_index].frequency >= self.heap[index].frequency:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_parent(self, index):
        return (index - 2) // 2

    def heapify(self, array):
        self.heap = []

        if array is None:
            return

        for item in array:
            self.insert(item)

    def pop(self):
        root = self.heap.pop(0)
        self.heapify(self.heap)
        return root

    def __repr__(self):
        return str(self.heap)


def huffman_encoding(data):
    frequencies = {}

    for char in data:
        node = frequencies.setdefault(char, Node(char))
        node.frequency += 1

    minHeap = MinHeap(list(frequencies.values()))


def huffman_decoding(data, tree):
    pass


if __name__ == "__maien__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
myheap = MinHeap()
myheap.insert(Node("a", 40))
myheap.insert(Node("b", 30))
myheap.insert(Node("c", 20))
myheap.insert(Node("d", 10))
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)


myheap = [40, 30, 20, 10]
heapify(myheap)
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
# Test Case 2

# Test Case 3
