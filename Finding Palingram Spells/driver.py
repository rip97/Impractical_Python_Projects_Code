# Filename: driver.py
# @author: rip97
# Date: 9/21/2024
# Description: main file for execution of program of finding paligrams

import Functions


def main():
    # load list of words & create empty list
    file_name = "C:\\Users\\jripp\\git\\Python\\Impractical Python Projects\\Impractical_Python_Projects_Code\\Dictionarys\\dictionary1.txt"
    words = Functions.open_dictionary(file_name)

    ''' 
    loop through list 
        if current word equals reversed word add to list of palindroms
        
    '''
    palin_list = findPalinDromes(words)

    print("Here is a list of palindromes from your file:")
    print(*palin_list, sep="\n")

    # finding palingrams






def findPalinDromes(word_list):

    palin_list = []
    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palin_list.append(word)

    return palin_list




if __name__ == '__main__':
    main()