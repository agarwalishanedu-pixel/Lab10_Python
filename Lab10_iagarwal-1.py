"""
Program Name: Lab 10
My name: Ishan Agarwal
Purpose: To better understand Object oriented programming, exception handling, path library, string manipulation, and dependency management
Starter Code: None
Date: 03/29/2026
"""

#Import
from pathlib import Path
import string

class WordAnalyzer:
    """
    This class is used to handle, process, and read text files, and count frequencies then produce an output. 
    """

    def __init__(self, filepath: str):
        """
        This function stores the file path and initializes the dictionary.
        """

        self.__filepath: Path = Path(filepath)
        self.__frequencies: dict[str, int] = {}





