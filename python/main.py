#!/usr/bin/python3
# -----------------------------------------------------------------
# Huffman code implementation using python.
#
#
#
# Author:N84.
#
# Create Date:Wed Apr  5 03:38:19 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------

from utils import *
import math
from time import sleep


def find_binary_source_entropy(message: str):
    """
        :ARGS:
            message:str => the message we want to find its binary entropy.

        :RETURNS:
            return float, "bit/symbol";

        :INFO:
            we define this as a Logarithmic scale for data transfer in rate in a message;
            and its the minimum amount of bits that exist in a symbol;
    """

    assert isinstance(
        message, str), f"message must be a str type not {type(message)}"

    symbol_count = len(message)

    symbol_probabilities = message_symbols_probability(message)

    return sum((symbol_probabilities[char] * math.log2(1/symbol_probabilities[char])) for char in set(message))


def find_max_binary_source_entropy(message: str):
    """
        :ARGS:
            message:str => the message we want to find the max binary source entropy;

        :RETURNS:
            return int;

        :INFO:
            find the max binary entropy for the given message;
    """

    assert isinstance(
        message, str), f"message must be a str type not {type(message)}"

    symbol_count = len(message)

    # approximate the symbol count to the greater nearest 2^n;
    symbol_count = math.ceil(math.log2(symbol_count))

    return int(math.log2(symbol_count))


def find_message_redundancy(message: str):
    """
        :ARGS:
            message:str => message we want to find the redundancy for it;

        :RETURNS:
            return float;

        :INFO:
            find the redundancy for the given message, and its defined as:
                "the difference between the max binary entropy for the message and,
                 the actual binary entropy for the message"
    """

    return find_max_binary_source_entropy(message) - find_binary_source_entropy(message)

def find_coding(node:Node, codes:dict=None, code=""):
    """
        :ARGS:

        :RETURNS:
            return list;

        :INFO:

    """
    
    if codes is None:
        codes = dict()
    
    if node is None:
        return None
    
    code += node.code
    
    if not node.symbol is None:
        codes[node.symbol] = code
    
    find_coding(node.left, codes, code)
    find_coding(node.right, codes, code)
    
    return codes


def main():

    
    # TEST_MESSAGE = "A" * 5 + "B" * 6 + "C" * 9 + "D" * 12

    characters_frequency = message_symbols_frequency(TEST_MESSAGE)
    
    sorted_char_dict = sorted(characters_frequency, key=lambda k: characters_frequency[k], reverse=False)
    
    sorted_chars = {key: characters_frequency[key] for key in sorted_char_dict}
    
    
    nodes = [Node(symbol=char, frequency=freq) for char, freq in sorted_chars.items()]
    
    # print(nodes)
    while len(nodes) > 1:
        
        new_node = Node()
        
        nodes = sorted(nodes, key=lambda node: node.frequency)
        
        smaller_node1, smaller_node2 = nodes[0:2]
        
        new_node.frequency = smaller_node1.frequency + smaller_node2.frequency
        
        smaller_node1.code = "1"
        smaller_node2.code = "0"
        
        new_node.left = smaller_node1
        new_node.right = smaller_node2
        
        nodes[0:2] = [new_node]

    
    
    root = nodes[0]
    
    
    # code = root.right.code + root.right.right.code + root.right.right.right.code
    codes = find_coding(root)
    
    encoded_text = "".join(codes[char] for char in TEST_MESSAGE)
    
    print(encoded_text)
        
    
    
    
 

if __name__ == "__main__":
    main()
