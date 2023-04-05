"""
    Contain all needed tools for this project;
"""

from os import system
from os import name
import math

OS_NAME = name


def clear():
    """
        :ARGS:
            None;

        :RETURNS:
            return None;

        :INFO:
            wipe terminal screen;
    """

    if OS_NAME == "posix":
        # for *nix machines;
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other os in this world;
        # system("your-command-here")
        pass

    return None
