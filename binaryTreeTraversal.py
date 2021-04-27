class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''        1
    2           5
3       4
'''
myNode = Node(1)
myNode.left = Node(2)
myNode.left.left = Node(3)
myNode.left.right = Node(4)
myNode.right = Node(5)

def inNodeTraversal(root):
    curr = root
    stack = []
    done = 0
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.data)
            curr = curr.right
        else:
            break

inNodeTraversal(myNode)
                
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

inNodeTraversal(root)


# def diffBetweenTwoStrings(source, target):
#     src, dst = len(source), len(target)
#     res = []
#     stack = [[None for _ in src]] * dst

text = "Dear hiring manager, I\
    am graduate student of computer science with passion and skills for infrastructure \
    automation in ultra-large scale and fast paced environment.\
    You will love to have me in your team. Regards."

print(len(text), len(text.split()))
