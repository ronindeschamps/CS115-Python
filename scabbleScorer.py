#Ronin Deschamps
#I pledge my honor that I have abided by the Stevens Honor System

'''
Created on _______________________
@author:  Ronin Deschamps
Pledge:   I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2
'''


import sys

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo','spam', 'spammy', 'zzyzva']

def letterScore(letter, scorelist):
    if len(scorelist) == 0:
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    if len(S) == 0:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def removeAll(e, L):
    if L == []: 
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def wordcheck(word, Rack):
    if word == "":
        return True
    if word[0] in Rack :
        return wordcheck(word[1:], removeAll(word[0], Rack))
    return False

def wordlist(Dictionary, Rack):
    return filter(lambda word: wordcheck(word, Rack), Dictionary)

def wordscore2(word):
    return [word, wordScore(word, scrabbleScores)]

def scoreList(Rack):
    return list(map(wordscore2, wordlist(Dictionary, Rack)))

def bestWord(Rack):
    list1 = scoreList(Rack)
    if list1 == []:
        return["", 0]
    return reduce(lambda x,y: x if x[1]>y[1] else y, list1)

            





    
    

        
    
    
        
        
        

    
    
