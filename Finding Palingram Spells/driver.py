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

    palingrams = find_palingrams(words)

    print("Here is the number of palingrams for your file: {}\n".format(len(palingrams)))
    for first, second in palingrams:
        print("{} {}".format(first,second))





def findPalinDromes(word_list):

    palin_list = []

    # for word in word_list:
    #    if len(word) > 1 and word == word[::-1]:
    #        palin_list.append(word)

    for word in word_list:
        if len(word) > 1:
            if palingdrome_recursive(word,0, len(word)-1):
                palin_list.append(word)

    return palin_list



def find_palingrams(word_list):

    palingram_list = []
    word_set = set(word_list)

    '''
    loop through words in word list
    get length of word 
    if length > 1 
        begin looping through letters in list 
            if reversed word fragment at front of word is in word list & letters after form
            a palindromic seq: 
                add word and reversed word to list 
            if reversed word fragment at end of word is in word list & letters before form 
            a palindromic seq:
                add reversed word and word to list
    '''
    for word in word_set:
        word_len = len(word)
        rev_word = word[::-1]

        if word_len > 1:
            for l in range(word_len):

                # if front end sliced reversed in word_list (a real word) & back end of word is palindromic is true
                if rev_word[word_len-l:] in word_set and word[l:] == rev_word[:word_len-l]:
                    # print(word, rev_word[:word_len-l])
                    palingram_list.append((word, rev_word[:word_len-l]))
                # if front end of word is palindromic & back end sliced in word list
                if rev_word[:word_len-l] in word_set and word[:l] == rev_word[word_len-l:]:
                    # print(rev_word[:word_len-l],word)
                    palingram_list.append((rev_word[:word_len-l], word))

    # return a sorted list
    return sorted(palingram_list)


def palingdrome_recursive(word, beg, end):

    if beg == end:
        return True
    if word[beg] != word[end]:
        return False
    if beg < end + 1:
        return word, beg + 1, end-1


if __name__ == '__main__':
    main()