#Ronin Deschamps
#I Pledge my honor that I have abided by the Stevens Honor System


'''should output the dot product of the lists L and K.
The dot product of two vectors or lists is the sum
of the products of the elements in the same position in the two vectors.'''
def dot(L, K):
    if L==[]: 
        return 0
    prod = L[0]*K[0]
    return prod + dot(L[1:], K[1:])


'''take a string S as input and should return a list of the characters'''
def explode(S):
    if S=='':
        return []
    return [S[0]] + explode(S[1:])

'''Returns the number of times e occurs in list L'''
def ind(e, L):
    if L==[] or L[0]==e:
        return 0
    return ind(e, L[1:])+1

'''Removes all instances of e in list L'''
def removeAll(e, L):
    if L==[]: 
        return []
    if L[0]==e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

'''checks weather a number is even'''
def even(x):
    if x % 2 == 0 : return True
    return False

'''takes a function and a list and returns all elements in the list that
are true for the given function'''
def myFilter(func, L):
    if L==[]:
        return []
    if (func(L[0])==True):
        return [L[0]] + myFilter(func, L[1:])
    return myFilter(func, L[1:])


'''This returns a list reversed, and will reverse all lists inside the list.'''
def deepReverse(L):
    if L==[]:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    return deepReverse(L[1:])+[L[0]]



        


    
    
        
