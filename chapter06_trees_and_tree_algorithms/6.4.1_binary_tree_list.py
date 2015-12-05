def binary_tree(r):
    return [r, [], []]
    
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    
    return root 
    
def insert_right(root, new_branch):
    t = root.pop(2)
    
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])
        
    return root 
    
def get_root_val(root):
    return root[0]
    
def set_root_val(root, new_val):
    root[0] = new_val
    
def get_left_child(root):
    return root[1]
    
def get_right_child(root):
    return root[2]

def build_tree():
    r = binary_tree('a')

    # left subtree 
    insert_left(r, 'b')
    insert_right(get_left_child(r), 'd')
    
    # right subtree 
    insert_right(r, 'c')
    insert_left(get_right_child(r), 'e')
    insert_right(get_right_child(r), 'f')
    
    return r 
    
print(build_tree())

    
