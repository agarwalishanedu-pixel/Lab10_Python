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

    def process_file(self):
        """
        This is the main logic, this does he counting of the words
        This also does the necessary exception handling
        """

        try:
            # To see if the file exists
            if self.__filepath.exists():
                file = self.__filepath.open("r", encoding = "utf-8")
            else:
                #Sends to the except block
                raise FileNotFoundError
            
            #This is to Remove punctuation
            translation = str.maketrans('', '', string.punctuation)

            #reading file, dividing it into line and then words (in lowercase). 
            for line in file:
                line = line.lower()
                line = line.translate(translation)
                words: list[str] = line.split()

                for word in words:
                    if word in self.__frequencies:
                        self.__frequencies[word] += 1
                    else:
                        self.__frequencies[word] = 1

            file.close()
            return True
            
        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def print_report(self):
        """
        This prints the output in alphabetical order
        """

        print()
    
        #sort the words alphabetically
        sorted_words = sorted(self.__frequencies.keys())

        for word in sorted_words:
            print(f"{word:<10} :: {self.__frequencies[word]}")
