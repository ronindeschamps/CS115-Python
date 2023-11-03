#Ronin Deschamps
#I pledge my honr that I have abided by the Stevens Honor System

'''base case will return a list containing 0, []'''

def knapsack(capacity, items):
    if items == [] or capacity <= 0:
        return [0, []]
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:]) #else if
    #statment will return capacity and items without the first element
    #if the first element is larget than the capcity.'''

    else:
        result = knapsack(capacity - items[0][0], items[1:]) #else statement takes a recusive
        #call and splits it into the recursed value
        #and recursed item
         #the next lines construct a use it or loose it system that has values and items separeted
        #so the items can be part of the output'''
        use_it_value = result[0] + items[0][1]
        use_it_items = [items[0]] + result[1]

        result = knapsack(capacity, items[1:])
        lose_it_value = result[0]
        lose_it_items = result[1]

        #these lines compare the values of use it or lose it and return the highest value plus the items
        #used to make that value
        
        if use_it_value > lose_it_value:
            return [use_it_value, use_it_items]
        else:
            return [lose_it_value, lose_it_items]



