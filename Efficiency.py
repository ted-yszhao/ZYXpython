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
def using_list_comprehension(n):
    return [k * k for k in range(n)]


@timer
def using_append(n):
    s = []
    for k in range(n):
        s.append(k * k)
    return s

@timer
def using_assign(n):
    s = [0 for k in range(n)]
    for k in range(n):
        s[k] = k * k
    return s

@timer
def using_insert(n):
    s = []
    for k in range(n):
        s.insert(0, k * k)
    return s

@timer
def using_add(n):
    s = []
    for k in range(n):
        s = s + [k*k]
    return s

n = int(1e5)
print(f'When n = {n}.')
using_list_comprehension(n)
using_add(n)
using_append(n)
using_assign(n)
using_insert(n)


