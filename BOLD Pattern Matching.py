# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:10:09 2021

@author: IT LAB
"""

from simple_colors import *
import pyperclip as pc
text=pc.paste()
print(text)
while True:
    print('Enter the word you would like to find')
    keyWord = input()
    if keyWord == '':
        print('Thank you for using basic search!')
    elif not keyWord.isalnum():
        print('Please enter a word or an alphanumeric string without spaces')
    else:
        wordList = text.split()
        matchCount = 0
        for i in range(len(wordList)):
            if wordList[i] == keyWord:
                wordList[i] = wordList[i].center((len(wordList[i])+4),'_')
                matchCount += 1
        print('There are %d matches to your key word, %s' % (matchCount,keyWord))
        print(green(keyWord,'bold'))
        newText = ' '.join(wordList)
        pc.copy(newText)
        print('Paste from clipboard in a Markdown cell to see the search results')
        break                           