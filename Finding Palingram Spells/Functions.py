# Filename: Functions.py
# @author: rip97
# Date: 9/21/2024
# Description: Store functions for main driver file

import sys

''' 
Load a dictionary file as a list

Args: -text file name (filepath if needed) 

Exceptions: I/O Error if filename not found 

Returns: List of all words in a text file as lowercase

Dependencies: import sys
'''

def open_dictionary(file):
    try:
        with open(file) as file_in:
            load_txt = file_in.read().strip().split("\n")
            load_txt = [words.lower() for words in load_txt]
            return load_txt
    except IOError as e:
        print("{}\nError in opening {}. Terminating program.",format(e, file), file=sys.stderr)
    sys.exit(1)
