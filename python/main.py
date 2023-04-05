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

    symbol_probabilities = message_chars_probability(message)

    return sum((symbol_probabilities[char] * math.log2(1/symbol_probabilities[char])) for char in set(message))


def main():

    # print(find_binary_source_entropy("AAAAABBCCD"))
    print(find_binary_source_entropy(TEST_MESSAGE))


if __name__ == "__main__":
    main()
