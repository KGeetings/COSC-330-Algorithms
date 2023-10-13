# Description: Huffman Code Implementation
# Author: Kenyon Geetings & Sam Scholz
# Class: COSC-330 Algorithms

import heapq

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

    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        z = Node(None, x.freq + y.freq)
        z.left, z.right = x, y
        heapq.heappush(heap, z)

    root = heap[0]
    huffman_codes = {}

    def traverse(node, code):
        if node.char:
            huffman_codes[node.char] = code
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")

    return huffman_codes

# Main
def main():
    # Input lines
    input_lines = [
        "a:45 b:13 c:12 d:16 e:9 f:5",
        "a:1 b:1 c:2 d:3 e:5 f:8 g:13 h:21",
        "m:20 n:22 o:18 p:24 r:20 t:17 w:26 x:16"
    ]

    # Input file
    input_file = open("huffmanCodeInput.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()

    for input_line in input_lines:
        huffman_codes = huffman(input_line)
        print("Input:", input_line)
        for char, code in huffman_codes.items():
            print(f"Character: {char}, Code: {code}")
        print()

if __name__ == "__main__":
    main()
