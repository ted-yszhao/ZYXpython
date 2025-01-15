

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



class Link:
    empty = () # empty tuple 
    def __init__(self,first , rest=empty):

        assert rest is Link.empty or isinstance(rest, Link)

        self.first = first 
        self.rest = rest

    def __repr__(self):
        """

        Returns:
            _type_: _description_
        """

        if self.rest is Link.empty:
            return f'Link({self.first})'
        else:
            return f'Link({self.first},{self.rest.__repr__()})'

    def __str__(self):
        """ [1,2,3,4,5]
        [1] [2,3,4,5]
        Returns:
            _type_: _description_
        """
        result = '['
        s = self
        while not s is Link.empty:
            result +=str(s.first) + ', '
            s = s.rest
        return result[:len(result) - 2] + ']'
        

@timer
def double(s,v):
    """Insert anoher v after each v in list s

    Args:
        s (_type_): _description_
        v (_type_): _description_

    s = [1,2,3,2,1]
    double(s,2)
    s = [1,2,2,3,2,2,1]
    """

    i = 0 
    while i < len(s):
        if s[i] == v:
            s.insert(i+1,v)
            i += 2
        else:
            i += 1

@timer
def double_link(s , v):
    """Insert another v after each v in Link s

    Args:
        s (_type_): _description_
        v (_type_): _description_
    """
    while not s is Link.empty:
        if s.first ==v:
            n=Link(v,s.rest)
            s.rest=n
            s=n.rest
        else:
            s=s.rest


@timer
def cycle(k ,n):
    """Build an n-element list that cucles among range(k)


    Args:
        k (_type_): _description_
        n (_type_): _description_


    >>> cycle(3,10)
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """

    s = []
    for i in range(n):
        s.append(i % k)
    return s


@timer
def cycle_link(k , n ):
    first=Link.empty
    for i in range (n):
        new_node=Link(i%k)
        if first is Link.empty:
            first, last= new_node, new_node
        else:
            last.rest,last= new_node, new_node
    return first

# n = int(50000)
# double(cycle(5,n) , 3)

# double_link(cycle_link(5,n) , 3)

def slice_link(s, i , j):

    """
    >>> s = [1,2,3,4,5]
    s[1:3]
    [2 ,3]

    s[i:j]
    """

    # iterative approach 
    # new_link=s
    # for _ in range(i):
    #     new_link=new_link.rest
    # first=Link.empty
    # for _ in range(j-i):
    #     if first is Link.empty:
    #         first=Link(new_link.first)
    #         last=first
    #     else:
    #         last.rest=Link(new_link.first)
    #         last=last.rest
    #     new_link=new_link.rest
    # return first
    
    # recursive approach 

    # 1st base case 
    if s is Link.empty or j == 0:
        return Link.empty
    # 2nd base case 
    if i == 0:
        return Link(s.first, slice_link(s.rest , 0 , j - 1))
    
    return slice_link(s.rest , i - 1 , j - 1)
    

def insert_link(s , x , i):
    """Insert x into linked list s at index i
    s = [2,3,4]
    insert_link(s, 5, 0)
    s = [5 , 2,3, ,4]
    Args:
        s (_type_): _description_
        x (_type_): _description_
        i (_type_): _description_
    """
    # iterative approach 
    # i_link=s
    # j=0
    # while j<i:
    #     if i_link is Link.empty:
    #         return "Index out of range."
    #     j+=1
    #     i_link=i_link.rest

    # new_link=Link(i_link.first,i_link.rest)
    # i_link.first, i_link.rest=x,new_link

    # recursive approach 

    if s is Link.empty:
        return 'Index out of range'
    elif i == 0:
        second = Link(s.first , s.rest)
        s.first , s.rest = x , second
    else:
        insert_link(s.rest, x , i- 1)

l1 = Link( 4 , Link ( 3 , Link(4, Link (5, Link(3)))))

insert_link(l1, 10, 2)

print(l1)