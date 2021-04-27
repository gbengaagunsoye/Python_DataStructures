"""
In BFS we must finish exploring a node before moving to the next node
Exploration means visiting all adjacent nodes to the curr node

"""
from collections import deque
q = deque()
def breadthFirstSearch(rootNode):
    if rootNode == None:
        return
    else:
        curr = rootNode
        print(curr.vertex)
        # q.append(curr)
        q.append(curr.left)
        q.append(curr.right)
    while q:
        curr = q.popleft()
        breadthFirstSearch(curr)





class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.left = None
        self.right = None

"""       
    #                   10
                    /       \
    #         5                   2
#           /   \               /   \
    #     3       0           8          6
                /   \                   /  \
    #           3   4                  9    6    
"""

root = Node(10)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(0)
root.left.right.left = Node(3)
root.left.right.right = Node(4)
root.right.left = Node(8)
root.right.right = Node(6)
root.right.right.left = Node(9)
root.right.right.right = Node(6)

# 10,5,2,3,0,8,6,3,4,9,6
#10,5,

breadthFirstSearch(root)



"""
from collections import deque

q = deque()
visited = []

def breadthFirstSearch(rootNode):
    if rootNode == None:
        return
    else:
        curr = rootNode
        # print(curr.vertex)
        q.append(curr)
        q.append(curr.left)
        q.append(curr.right)
    while q:
        curr = q.popleft()
        breadthFirstSearch(curr)

"""

