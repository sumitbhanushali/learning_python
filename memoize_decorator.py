import functools

#lru_cache takes to optional arugments
#maxsize and typed(boolean)
#maxsize is size of results to store for memoizing
#when typed is true ints and floats are treated differently
#lru_cache(maxsize=128,typed=False)
#for optimal perfmance keep value of maxsize power of 2
@functools.lru_cache() #memoization 
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(30))