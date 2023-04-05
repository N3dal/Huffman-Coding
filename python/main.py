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


def main():

    # print(find_binary_source_entropy("AAAAABBCCD"))
    # print(find_binary_source_entropy(TEST_ME`SSAGE))
    # print(find_max_binary_source_entropy(TEST_MESSAGE))
    # print(find_message_redundancy(TEST_MESSAGE))

    symbols_prob = message_symbols_probability(TEST_MESSAGE)

    for key in sorted(symbols_prob, key=lambda k: symbols_prob[k]):
        print(f"'{key}' => {round(symbols_prob[key] * len(TEST_MESSAGE))}")


if __name__ == "__main__":
    main()
