# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:45:59 2018
@author: sourav ghosh
"""
"""
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint:​ ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
"""
wordslist = ['ab','cde','erty']
print(list(map(lambda x: len(x), wordslist)))

"""Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""

def isvowel(string):
    vowelstuple = ('a','e','i','o','u')
    if string in vowelstuple:
        return True
    else:
        return False
string = input("Enter a character: ")
print(isvowel(string.lower())) #Output : User may key in either lowercase or uppercase character, so convert the input character in lowercase and check if it's a vowel or not