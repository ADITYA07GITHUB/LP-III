
import heapq

def huffman(characters, frequencies):
    heap = []

    for i in range(len(characters)):
        heapq.heappush(heap, (frequencies[i], i, characters[i]))

    count = len(characters)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = (left[0] + right[0], count,
                    (left[2], right[2]))

        heapq.heappush(heap, new_node)
        count += 1

    def print_codes(node, code=""):
        if isinstance(node, str):
            print(node, ":", code or "0")
            return

        print_codes(node[0], code + "0")
        print_codes(node[1], code + "1")

    print("\nHuffman Codes:")
    print_codes(heap[0][2])


n = int(input("Enter number of characters: "))

characters = []
frequencies = []

for i in range(n):
    ch = input("Enter character: ")
    freq = int(input("Enter frequency: "))

    characters.append(ch)
    frequencies.append(freq)

if n > 0:
    huffman(characters, frequencies)
else:
    print("Enter at least one character.")

##time complexity of huffman coding is O(nlogn) and space complexity is O(n)


# Line-by-Line Explanation
# Step 1: Import heapq
# import heapq



# - heapq is a built-in Python module.
# - It implements a min-heap.
# - A min-heap keeps the smallest element at the top.
# Why do we use it?

# Because Huffman Encoding always selects the two nodes with the lowest frequencies.
# Step 2: Define the function
# def huffman(characters, frequencies):    heap = []



# - def creates a function.
# - characters stores letters like A, B, C.
# - frequencies stores how many times each letter occurs.
# - heap = [] creates an empty list.
# Example:
# characters = ['A', 'B', 'C', 'D']frequencies = [5, 9, 12, 13]



# Step 3: Insert characters into the heap
# for i in range(len(characters)):    heapq.heappush(heap, (frequencies[i], i, characters[i]))



# Explanation:
# - len(characters) counts the number of characters.
# - for repeats for every character.
# - heappush() inserts an element into the min-heap.
# Each element contains three values:

# (frequency, index, character)

# Example:
# (5, 0, 'A')
# (9, 1, 'B')
# (12, 2, 'C')
# (13, 3, 'D')


# The index is used to break ties when frequencies are equal.
# Step 4: Initialize count
# count = len(characters)



# For four characters:
# count = 4


# This gives every newly created internal node a unique number.
# Step 5: Build the Huffman Tree
# while len(heap) > 1:



# Meaning: Continue until only one node remains in the heap.

# Why?

# Because the final remaining node is the root of the Huffman Tree.
# Step 6: Remove two minimum frequencies
# left = heapq.heappop(heap)right = heapq.heappop(heap)



# heappop() removes and returns the smallest element.

# Example:
# left  = (5, 0, 'A')
# right = (9, 1, 'B')


# So we select A and B.
# Step 7: Combine the frequencies
# new_node = (left[0] + right[0], count,            (left[2], right[2]))



# Let's understand:
# - left[0] = 5
# - right[0] = 9
# - left[0] + right[0] = 14
# - count = 4
# - left[2] = 'A'
# - right[2] = 'B'
# New node:
# (14, 4, ('A', 'B'))



# This means A and B are combined into a new parent node with frequency 14.
# Step 8: Insert new node
# heapq.heappush(heap, new_node)count += 1



# - Inserts the combined node back into the heap.
# - Increases count by 1.
# Now the heap contains nodes with frequencies:
# 12, 13, 14


# The process repeats:
# 12 + 13 = 25
# 14 + 25 = 39


# Finally, only the root node with frequency 39 remains.
# 3. Generate Huffman Codes
# def print_codes(node, code=""):



# This function generates binary codes using recursion.

# Initially, code is an empty string.
# if isinstance(node, str):    print(node, ":", code or "0")    return



# Explanation:
# - isinstance(node, str) checks whether the current node is a character.
# - If yes, it prints the character and its binary code.
# - return stops recursion for that character.
# - code or "0" ensures a single character receives the code 0.
# Now:
# print_codes(node[0], code + "0")print_codes(node[1], code + "1")



# These are recursive calls.
# - Left branch = 0
# - Right branch = 1
# For example, to reach A, we go left twice:
# Root → Left (0) → Left (0) → A

# Code of A = 00


# 4. User Input Explanation
# n = int(input("Enter number of characters: "))



# Takes the total number of characters.
# characters = []frequencies = []



# Creates two empty lists.
# for i in range(n):    ch = input("Enter character: ")    freq = int(input("Enter frequency: "))



# Takes the character and frequency from the user.
# characters.append(ch)frequencies.append(freq)



# append() adds values to their respective lists.

# Example:
# characters = ['A', 'B', 'C', 'D']
# frequencies = [5, 9, 12, 13]


# Finally:
# if n > 0:    huffman(characters, frequencies)else:    print("Enter at least one character.")



# This calls the Huffman function when at least one ch