###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import time
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    result = 0
    if (target_weight, egg_weights) in memo:
        return memo[target_weight, egg_weights]
    elif target_weight == 0 or egg_weights == ():
        return 0
    elif egg_weights[-1] > target_weight:
        return dp_make_weight(egg_weights[:-1], target_weight, memo)
    else:
        newItem = egg_weights[-1]
        withVal = 1 + dp_make_weight(egg_weights, target_weight - newItem, memo)
        withoutVal = dp_make_weight(egg_weights[:-1], target_weight, memo)
        if withVal < withoutVal or withoutVal == 0:
            result = withVal
        else:
            result = withoutVal
        memo[(target_weight, egg_weights)] = result
    return result
    

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    start = time.time()
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    end = time.time()
    print(end - start)
    