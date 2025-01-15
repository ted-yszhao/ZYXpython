class Tree:
    def __init__(self , label , branches= []):
        for branch in branches:
            assert Tree.is_tree(branch)

        self.label = label
        self.branches = branches

    def is_tree(self):
        return isinstance(self,Tree) and all([Tree.is_tree(b) for b in self.branches])
    
    def __str__(self):
        """Tree(label, [branchhes])

        Returns:
            _type_: _description_
        """

        if len(self.branches) == 0:
            return f'Tree({self.label})'
        else:
            return f'Tree({self.label} , {[branch.__str__() for branch in self.branches]})'
    

# f(n) = f(n-1) + f(n-2) f(0)=0  f(1) = 1


import time

def timer(func):
    """A decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record the end time
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper


@timer
def fib_tree(n):
    if n == 0 or n== 1:
        return Tree(n)
    else:
        left = fib_tree(n-1)
        right = fib_tree(n-2)
        return Tree (left.label + right.label , [left, right])


# # exponential growth 
# for i in range(30):
#     fib_tree(i)

# memoization 

def memo(f):
    cache = {} # key :  value pair
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

print(memo(fib_tree)(10))