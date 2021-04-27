"""
OS question
- Process vs Thread
- Kernel Thread vs User Space Thread
- How OS boots, list the operations
- Semaphores and mutexes
- Multiprocess and multithread questions
Answer Question
Algorithm and DS questions
- All sort algorithms you know and their complexity
- Why sorting algorithms are an important topic in CS
- Some Tree, Hash map (chaining) and stack questions
- For storing <IP addr,, other data> pairs, which data structures you could use other than a hash table?
Answer Question
C language question
- Stack vs heap memory
- Pointers
- Find the error in the C code (about stack memory)
- What is the output of the code (uses static variable)
Answer Question
Coding questions
- Print items in the list that has #odd w/o any additional memory space {3,3,4,3,1,1} ==> 3,3,4,3
- Remove multiple spaces and tabs from the string and count the number of them
- Reverse the order of the words in the sentence
- Two sum: find the number of pairs with sum=K, do not use the same numbers/pairs twice


"""

def visit(Node,res):
   if Node.data is not None:
      res.append(Node.data)
    # print(Node.data)

def InOrderTraversal(Node, res):
    if Node is None:
        return
    InOrderTraversal(Node.left, res)
    visit(Node, res)
    InOrderTraversal(Node.right, res)
    return res

def preOrderTraversal(Node, res):
    if Node is None:
        return
    visit(Node, res)
    preOrderTraversal(Node.left, res)
    preOrderTraversal(Node.right, res)
    return res

def postOrderTraversal(Node, res):
    if Node is None:
        return
    postOrderTraversal(Node.left, res)
    postOrderTraversal(Node.right, res)
    visit(Node, res)
    return res

class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         temp.left = TreeNode(data)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         temp.right = TreeNode(data)
         break
      else:
         que.append(temp.right)
def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree



root = make_tree([10,5,15,2,7,None,20])
print(InOrderTraversal(root, []))
print(preOrderTraversal(root, []))
print(postOrderTraversal(root, []))

            #            10
            #     5              15
            # 2       7      None      20
