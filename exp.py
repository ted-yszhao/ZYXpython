def tree(label,branches=[]):
    """ Construct a tree given its label and branches

    Args:
        label (_type_): _description_
        branches (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    for branch in branches:
        assert is_tree(branch)
    return [label] + branches
    

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return branches(tree) == []

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    
    return True

t = tree(
    1,
    [
        tree(2),
        tree(2,[
            tree(1),
            tree(1)
        ])
    ]
)

def above_root(tree):
    def process(u):
        if label(u)>label(tree):
            print (label(u))
        for branch in branches(u):
            process(branch)
    process(tree)

above_root(t)