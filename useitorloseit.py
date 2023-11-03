#Ronin Deschamps
#I pledge my honor that I have abided by the Stevens Honor System

def change(amount, coins):
    #This base case will return infinity if the list coins is empty 
    if len (coins)==0 and amount>0:
        return float("inf")
#This if statement will return 0 when the amount is less than or equal to zero
    if amount<=0:
        return 0
    
    elif coins[0]>amount:
        #This recusive step will return the amount and the list of coins 
        #without the first item of the list if that item is larger than the amount
        return change(amount, coins[1:])
    else:
        #These two recursive steps run two separate sequences until all outcomes
        #have occured
        use_it = 1+change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)



