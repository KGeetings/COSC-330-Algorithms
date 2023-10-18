# Description: Huffman Code Implementation
# Author: Kenyon Geetings & Sam Scholz
# Class: COSC-330 Algorithms

class MinQueue:
    def __init__(self):
        self.minQ = []

    def insert(self, item):
        self.minQ.append(item)
        self._heapify_up(len(self.minQ) - 1)

    def extract_min(self):
        if len(self.minQ) == 0:
            return None
        if len(self.minQ) == 1:
            return self.minQ.pop()
        root = self.minQ[0]
        self.minQ[0] = self.minQ.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.minQ[index] < self.minQ[parent_index]:
                self.minQ[index], self.minQ[parent_index] = self.minQ[parent_index], self.minQ[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (left_child_index < len(self.minQ) and self.minQ[left_child_index] < self.minQ[smallest]):
            smallest = left_child_index
        if (right_child_index < len(self.minQ) and self.minQ[right_child_index] < self.minQ[smallest]):
            smallest = right_child_index
        if smallest != index:
            self.minQ[index], self.minQ[smallest] = self.minQ[smallest], self.minQ[index]
            self._heapify_down(smallest)


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman(input_string):
    char_freq = {}
    for pair in input_string.split():
        char, freq_str = pair.split(":")
        freq = int(freq_str)
        char_freq[char] = freq

    minQ = MinQueue()
    for char, freq in char_freq.items():
        minQ.insert(Node(char, freq))

    while len(minQ.minQ) > 1:
        x = minQ.extract_min()
        y = minQ.extract_min()

        z = Node(None, x.freq + y.freq)
        z.left = x
        z.right = y
        minQ.insert(z)

    root = minQ.minQ[0]
    huffman_codes = {}

    def traverse(node, code):
        if node.char:
            huffman_codes[node.char] = code
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")

    return huffman_codes


def main():
    readFromFile = False

    if readFromFile:
        input_file = open("huffmanCodeInput.txt", "r")
        input_lines = input_file.readlines()
        input_file.close()
    else:
        input_lines = [
            "a:45 b:13 c:12 d:16 e:9 f:5",
            "a:1 b:1 c:2 d:3 e:5 f:8 g:13 h:21",
            "m:20 n:22 o:18 p:24 r:20 t:17 w:26 x:16"
        ]

    for input_line in input_lines:
        huffman_codes = huffman(input_line)
        print("Input:", input_line)
        for char, code in huffman_codes.items():
            print(f"Character: {char}, Code: {code}")
        print()

if __name__ == "__main__":
    main()