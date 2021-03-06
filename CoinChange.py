# Return a list representing a coin system
# that contains coins from pennies up to
# one hunder dollar bills
# NOTE: All of your coins/bills 
# should be of the data type float
def init_StdSystem():
    '''
    >>> init_StdSystem()
    [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    '''
    return [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

# Write a function that makes a 
# list containing all of the standard 
# coins up to the inputted max coin value.
# If max_val is none, return the standard system.
def init_CoinSystem(max_val):
    '''
    >>> init_CoinSystem(5)
    [5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(1)
    [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(-1)
    'error'
    '''
   try:
    
    strd_lst = init_StdSystem()
    i = 0
    while strd_lst[i] > max_val:
        i +=1
    return strd_lst[i:len(strd_lst)]     
   
   except:
    return "error"




# Write a function that takes in a coin system
# and creates a dictionary that contains 
# each coin as a key with each coin having
# an associated value of 0.  
def init_ChangeDict(coin_system):
    '''
    >>> C = init_CoinSystem(1)
    >>> init_ChangeDict(C)
    {1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    >>> S = init_StdSystem()
    >>> init_ChangeDict(S)
    {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    '''
    coin_dict = {}
    for i in coin_system:
        coin_dict[i] = 0
    return coin_dict    

# Check if it is possible to give 
# exact change with the given coin system
# For simplicity's sake, you should just
# check that the money is at least greater than
# the smallest available coin. 
def isValidChange(money, coin_system):
    '''
    >>> S = init_StdSystem()
    >>> isValidChange(.001, S)
    False
    >>> isValidChange(.15, S)
    True
    '''
    min_coin = min(coin_system)
    if money >= min_coin:
        return True
    else:
        return False

# If coin change cannot be made, return an error message. 
# Return a tuple in the form (min_coins, coin_dict)
# where min_coins is the minimum number of coins required
# and coin_dict is a dictionary that returns how many
# of each coin was used. 
def coinChange(money, max_coin_val=None):
    '''
    >>> coinChange(1)
    (1, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 1, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0})
    >>> coinChange(5.75)
    (3, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 1, 1.0: 0, 0.5: 1, 0.25: 1, 0.1: 0, 0.05: 0, 0.01: 0})
    '''
    std_coin_system = init_StdSystem()
    coin_system = init_CoinSystem(money)
    coin_dict = init_ChangeDict(std_coin_system)
    value = money
    if isValidChange(money, coin_system):
        for i in coin_system:
            while i <= value:
                coin_dict[i] += 1
                value -= i
                value = round(value, 2)
        
        min_coins = 0
        for i in coin_dict:
            amount = coin_dict.get(i)
            if amount > 0:
                min_coins += amount
        return (min_coins, coin_dict)






