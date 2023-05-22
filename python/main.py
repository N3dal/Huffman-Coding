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



class Message:
    """
        Docstring;
    """
    
    def __init__(self, text:str=None):
        self.__text = text
        
        self.__binary_source_entropy_value = None
        self.__max_binary_source_entropy_value = None
        self.__redundancy_value = None
        self.__characters_probability_value = None
        self.__characters_frequency_value = None

    
    def set_text(self, text:str):
        """

        """
        
        self.__text = text
        
        return None
    
    @property
    def text(self):
        
        return self.__text
    
    @property
    def binary_source_entropy(self):
        """
        :RETURNS:
            return float, "bit/symbol";

        :INFO:
            we define this as a Logarithmic scale for data transfer in rate in a message;
            and its the minimum amount of bits that exist in a symbol;
        """
    
        if not self.__binary_source_entropy_value:
            self.__binary_source_entropy_value= sum(
                (self.characters_probability[char] * math.log2(1/self.characters_probability[char]))
                for char in set(self.text)
                )
        return self.__binary_source_entropy_value

    @property
    def max_binary_source_entropy(self):
        """
        :RETURNS:
            return int;

        :INFO:
            find the max binary entropy for the given message;
        """
        
        if not self.__max_binary_source_entropy_value:
            # approximate the chars count to the greater nearest 2^n;
            characters_count = math.ceil(math.log2(len(self)))

            self.__max_binary_source_entropy_value =  int(math.log2(characters_count))
            
        return self.__max_binary_source_entropy_value
    
    @property
    def redundancy(self):
        """
        :RETURNS:
            return float;

        :INFO:
            find the redundancy for the given message, and its defined as:
                "the difference between the max binary entropy for the message and,
                 the actual binary entropy for the message"
        """
        
        if not self.__redundancy_value:
            self.__redundancy_value = self.max_binary_source_entropy - self.binary_source_entropy
    
        return self.__redundancy_value
    
    @property
    def characters_probability(self):
        
        if not self.__characters_probability_value:
            
            symbol_count = len(self.text)

            self.__characters_probability_value = {symbol: (self.text.count(symbol) / symbol_count) for symbol in set(self.text)}
        
        return self.__characters_probability_value
    
    @property
    def characters_frequency(self):
        if not self.__characters_frequency_value:
            

            self.__characters_frequency_value = {symbol: self.text.count(symbol) for symbol in set(self.text)}
        
        return self.__characters_frequency_value
    
    def __len__(self):
        return len(self.text)
    
class Node:
    """
        :ARGS:
            
            symbol:str => the symbol it self;
            
            frequency:int => the character frequency;
            
            left=None => the left leaf or node;
            
            right=None => the right leaf or node;

        :INFO:
            the Node for huffman tree;

    """
    
    def __init__(self, symbol:str=None, frequency:int=None, left=None, right=None):
        
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right
        
        # tree direction, this will be either '0' or '1';
        self.code = ''
        
    def children(self):
        """
        :ARGS:
            None;

        :RETURNS:
            return Tuple;

        :INFO:
            return the children for this node;
        """
        
        return (self.left, self.right)
    
    def __str__(self):
        return f"[{self.left}<-({self.symbol}, {self.frequency})->{self.right}]"

    def __repr__(self):
        return self.__str__()

class HuffmanTree:
    """
        Docstring;
    """
    
    def __init__(self, message:Message):
        self.message = message
        self.root = None
        
        self.__setup_tree()
            
    def __setup_tree(self):
        sorted_char_dict = sorted(self.message.characters_frequency, key=lambda k: self.message.characters_frequency[k], reverse=False)
        
        sorted_chars = {key: self.message.characters_frequency[key] for key in sorted_char_dict}
        
        nodes = [Node(symbol=char, frequency=freq) for char, freq in sorted_chars.items()]
        
        # print(nodes)
        while len(nodes) > 1:
            
            new_node = Node()
            
            nodes = sorted(nodes, key=lambda node: node.frequency)
            
            smallest_node_1, smallest_node_2 = nodes[0:2]
            
            new_node.frequency = smallest_node_1.frequency + smallest_node_2.frequency
            
            smallest_node_1.code = "1"
            smallest_node_2.code = "0"
            
            new_node.left = smallest_node_1
            new_node.right = smallest_node_2
            
            nodes[0:2] = [new_node]

        
        
        self.root = nodes[0]
        
        return None

class HuffmanCompressor:
    """
        Docstring;
    """
    
    def __init__(self):
        pass
    
    def generate_map(self, node:Node, codes:dict=None, code:str=""):
        """
            :ARGS:
                node: Node => the root node to start tracing back and encoding the symbols;
                
                codes: dict => encoding map;
                
                code: str => temporally var to store the codes;

            :RETURNS:
                return dict;

            :INFO:
                generate the encoding and decoding map;

        """
        
        if codes is None:
            codes = dict()
        
        if node is None:
            return None
        
        
        code += node.code
        
        if not node.symbol is None:
            codes[node.symbol] = code
        
        self.generate_map(node.left, codes, code)
        self.generate_map(node.right, codes, code)
        
        return codes

    def encode(self, encoding_map:dict, msg:str):
        """
            :ARGS:
                encoding_map: dict => encoding map;
            
                msg: str => msg we want to encode;
                
            :RETURNS:
                return dict;

            :INFO:
                encode the msg simply out return the stream bits;
        """
        
        return "".join(encoding_map[char] for char in msg)

    def decode(self, decoding_map:dict, msg:str):
        """
            :ARGS:
                decoding_map: dict => decoding map;
            
                msg: str => msg we want to decode;
                
            :RETURNS:
                return str;

            :INFO:

        """
        
        decoded_msg = ""
        
        
        temp_code = ""
        
        assert isinstance(decoding_map, dict), f"decoding_dictionary must be a dict type!"
        assert isinstance(msg, str), f"msg must be a str type!"
        
        # now flip the keys and values of the decoding dictionary;
        flipped_decoding_dictionary = {value: key for key, value in decoding_map.items()}
        
        msg = list(msg)
        
        while msg:
            temp_code += msg.pop(0)
            
            if temp_code in flipped_decoding_dictionary:
                decoded_msg += flipped_decoding_dictionary[temp_code]
                temp_code = ""
                
        
        return decoded_msg
    
    @staticmethod
    def find_compression_percentage(original_msg:str, encoded_msg:str):
        
        percentage = round(100 - len(encoded_msg) / (len(original_msg) * 8) * 100, 2)
        
        return f"{percentage}%"
        
    
def main():
    # random_text = generate_random_text(length=10000)
    # print(random_text)
    
    
    msg = Message(TEST_MESSAGE_3)
    
    tree = HuffmanTree(msg)
    
    compressor = HuffmanCompressor()
    
    encoding_map = compressor.generate_map(tree.root)
    
    # print(encoding_map)
    
    encoded_text = compressor.encode(encoding_map, msg.text)

    decoded_text = compressor.decode(encoding_map, encoded_text)

    print(decoded_text == msg.text)
    print(compressor.find_compression_percentage(msg.text, encoded_text))
    
    # byte_array = bytearray(list(map(int, encoded_text)))
    
    # with open(r"./output.bin", "wb") as file:
    #     file.write(byte_array)
    
    # print(byte_array)


    
    
 

if __name__ == "__main__":
    main()
