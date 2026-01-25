"""
Top-down dynamic programming starts w/ the full problem 
and breaks it into smaller sub-problems using RECURSION

Memorisation - storing answers to sub-problems th first time we compute them so we never redo the work

We store the answers to the sub-problems in the cache by mapping the inputs to the outputs
cache[input] = output
for climbStairs(5), in the end...
cache = {1:1, 2:2, 3:3, 4:5, 5:8}
"""

# climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)

# climbStairs(1) = 1
# climbStairs(2) = 2
# climbStairs(3) = 3
# climbStairs(4) = 5
# climbStairs(5) = 8

def climbStairs(n: int) -> int:
    # saving answers as we compute them 
    cache = {} # "hash map"
    """cannot be inside climb func cause everytime it 
    is called, it will be reset to the empty dictionary"""
    def climb(stair):
        # base case
        if stair <= 2:
            return stair
        if stair in cache:
            # if 4 is in cache, don't recompute/recalculate
            return cache[stair]
        # recursive case
        answer = climb(stair-1) + climb(stair-2)
        cache[stair] = answer
        return answer

    return climb(n)