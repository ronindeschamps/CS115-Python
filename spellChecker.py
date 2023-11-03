'''
Created on 2/23/2023
@author:   Ronin Deschamps
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 5
'''
import time

words = []
HITS = 10

memo = {}
def fastED(first, second):
    
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    if (first, second) in memo:
        return memo[(first, second)]#this will return stored values if they are recursed
    
    if first == '':
        memo[(first, second)] = len(second)#This will store len(second) as a value in memo
        return len(second)#returns len(second) if first is empty
    
    elif second == '':
        memo[(first, second)] = len(first)#Store len(first) as a value in memo
        return len(first)
    
    elif first[0] == second[0]: 
        x = fastED(first[1:], second[1:])#sets x as the value of the revursive call
        memo[(first, second)] = x #stores the value of x in memo
        return x
    else:
        substitution = 1 + fastED(first[1:], second[1:]) 
        deletion = 1 + fastED(first[1:], second) 
        insertion = 1 + fastED(first, second[1:]) 
        x = min(substitution, deletion, insertion) #sets x to the min output of substitution, deletion, insertion
        memo[(first, second)] = x #stores the value of x in memo
        return x

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return list(map(lambda x: tuple([fastED(user_input, x)]+[x]), words))#maps a function that finds
#the edit distance and lists it with the word

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
