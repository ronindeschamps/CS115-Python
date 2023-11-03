'''
Created on 2/27/2023
@author:   Ronin Deschamps
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''

memo = {0:2, 1: 1}

def fast_lucas(n):
    if n in memo:
        return memo[n]
    else:
        x = fast_lucas(n-1)
        memo[n-1] = x
        y = fast_lucas(n-2)
        memo[n-2] = y
        z = x + y
        memo[n] = z
        return z
    
memo1 = {}

def fast_change(amount, coins):

    if (amount, tuple(coins)) in memo1:
        return memo1[(amount, tuple(coins))]
    
    #This base case will return infinity if the list coins is empty 
    if len (coins)==0 and amount>0:
        memo1[(amount, tuple(coins))] = float("inf")
        return float("inf")
#This if statement will return 0 when the amount is less than or equal to zero
    if amount<=0:
        memo1[(amount, tuple(coins))] = 0
        return 0
    
    elif coins[0]>amount:
        #This recusive step will return the amount and the list of coins 
        #without the first item of the list if that item is larger than the amount
        ans = fast_change(amount, coins[1:])
        memo1[(amount, tuple(coins[1:]))] = ans
        return ans
    else:
        #These two recursive steps run two separate sequences until all outcomes
        #have occured
        use_it = 1+fast_change(amount - coins[0], coins)
        lose_it = fast_change(amount, coins[1:])
        x = min(use_it, lose_it)
        memo1[(amount, tuple(coins))] = x
        return x

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


