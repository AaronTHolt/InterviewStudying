
class node_1(object):
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

def print_tree_inorder(node):
    '''inorder traversal and printing of tree'''
    
    #node left?
    if node.left!=None:
        print_tree_inorder(node.left)

    print node.data,

    #node right?
    if node.right!=None:
        print_tree_inorder(node.right)



def insert_node(node, data):
    '''Insert a node in sequential order'''
    if data == None:
        raise TypeError('Data must be numeric')

    #Base case: If no data, insert here
    if node.data == None:
        node.data = data
    #Data greater than pr equal to current node data
    elif data >= node.data:
        if node.right == None:
            node.right = node_1(parent=node, data=data)
        else:
            insert_node(node.right, data)
    #Data less than current node data
    elif data < node.data:
        if node.left == None:
            node.left = node_1(parent=node, data=data)
        else:
            insert_node(node.left, data)

def delete_data(root, data):
    '''Delete data if it exist'''




r = node_1(data=17)
for ii in range(0,30,4):
    insert_node(r, ii)

print_tree_inorder(r)
print ''
insert_node(r, 11)
insert_node(r, 27)
print_tree_inorder(r)
