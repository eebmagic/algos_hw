class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self, small=False, depth=0):
        if self.left:
            self.left.PrintTree(small=small, depth=depth+1)
        if small:
            print(self.data, depth)
        else:
            print(self.data, self)
            print(self.left, self.right)
        if self.right:
            self.right.PrintTree(small=small, depth=depth+1)


def find_depth(node):
    '''
    Gets the root node for the largest possible complete tree.
    Returns the depth of the tree and the root node.

    node: the current node in the traversal
    '''

    # if current node has less than two children
    # (can't be the root of a perfect tree larger than 0 edge depth)
    if node.left == None or node.right == None:
        return 0, node
    else:
        # Create two subproblems with two halves of tree
        # alpha = 2; beta = 2
        l = find_depth(node.left)[0]
        r = find_depth(node.right)[0]

        # Combine/select subproblem solutions and return
        if l == r:
            return l + 1, node
        elif l > r:
            return l, node.left
        elif l < r:
            return r, node.right


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

# root.insert(8)
# root.insert(13)
# root.insert(20)

# Tree where root is not answer
root.insert(9)
root.insert(1)
root.insert(5)
root.insert(7)
root.insert(10)


# Small test
root.PrintTree(small=True)
depth, node = find_depth(root)
print(f'\nFound depth of: {depth}')
print(f'Starting node: {node.data} = {node}')


# Random test
import random
MIN, MAX = 0, 50
n = 16
added = set()
large = Node((MAX-MIN)//2)
while len(added) < n:
    num = random.randint(MIN, MAX)
    while num in added:
        num = random.randint(MIN, MAX)
    large.insert(num)
    added.add(num)

large.PrintTree(small=True)
large_depth, large_node = find_depth(large)
print(f'\nFound depth of: {large_depth}')
print(f'Starting node: {large_node.data} = {large_node}')
