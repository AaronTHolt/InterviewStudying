
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
    elif delete_data < node.data:
        if node.left == None:
            node.left = node_1(parent=node, data=data)
        else:
            insert_node(node.left, data)

def delete_data(root, data):
    '''Delete data if it exist'''
    if root.data == data:
        return delete_node(root)
    elif data < root.data:
        if root.left:
            delete_data(root.left, data)
        else:
            return False
    else:
        if root.right:
            delete_data(root.right, data)
        else:
            return False




# def delete_node(node):
#     # temp_parent = node.Parent
#     temp_node = None

#     #root node?
#     if node.Parent == None:
#         node.data = None
#         return True

#     #no children
#     if node.left == None and node.right == None:
#         if node.Parent.left == node:
#             node.Parent.left = None
#         else:
#             node.Parent.right = None

#     #has one child
#     elif node.right != node.left:
#         if node.right:
#             temp_node = node.right
#         else:
#             temp_node = node.left

#         if node.Parent:
#             if node.parent.left == Node:
#                 node.parent.left = temp_node
#             else:
#                 node.parent.right = temp_node
#             del nod
#         else:
#             self.data = temp_node.data
#             self.left = temp_node.data
#             self.right = temp_node.right

#     #has 2 children
#     else:
#         parent = node
#         successor = node.right
        
#         while successor.left:
#             parent = successor.left
#             successor = successor.left
#         node.data = successor.data

#         if parent.left == successor:
#             parent.left = succerssor.right
#         else:
#             parent.right = successor.right










r = node_1(data=17)
for ii in range(0,30,4):
    insert_node(r, ii)

print_tree_inorder(r)
# print ''
# insert_node(r, 11)
# insert_node(r, 27)
# print_tree_inorder(r)
# delete_data(r, 11)
# print_tree_inorder(r)