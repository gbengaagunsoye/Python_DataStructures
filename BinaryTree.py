# In-order Traverse
# def inOrderTraversal(Node):
#     if Node is not None:
#         inOrderTraverse(Node.left)
#         visit(Node)
#         inOrderTraverse(Node.right)

# def preOrderTraversal(Node):
#     if Node is not None:
#         visit(Node)
#         preOrderTraverse(Node.left)
#         preOrderTraverse(Node.right)

# def postOrderTraversal(Node):
#     if Node is not None:
#         postOrderTraverse(Node.left)
#         postOrderTraverse(Node.right)
#         visit(Node)


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


class Solution(object):
   def inorderTraversal(self, root):
      res, stack = [], []
      current = root
      while True:
         while current:
            stack.append(current)
            current = current.left
         
         if len(stack) == 0:
            return res
         
         node = stack[-1]
         stack.pop(len(stack)-1)
         if node.data != None:
            res.append(node.data)
         current = node.right
      return res
ob1 = Solution()
root = make_tree([10,5,15,2,7,None,20])
print(ob1.inorderTraversal(root))

"""
[2,7], data = None
temp = 15
                        10
                5              15
            2       7      None      20

            if Node is not Node:
                inorderTravese(Node.left)
                visitNode
                inOrderTraverse(Node.right)

                output = 2,5,7,10,15,20

"""

class Solution2(object):
    def InorderTraversal(self, root, target):
        """
        def inOrderTraversal(node):
            if root is None:
                return
            inOrderTraversal(Node.left)
            visit(Node)
            inOrderTraversal(Node.right)
        """
        stack = []
        res = []
        curr = root
        sumSoFar = 0
        
        while True:
            while curr:
                if curr.data != None:
                    sumSoFar += curr.data
                if sumSoFar == target:
                    return sumSoFar
                if sumSoFar > target:
                    break
                stack.append(curr)
                curr = curr.left
            
            if not stack:
                return res
            
            
            node = stack[-1]
            stack.pop()     
            if node.data != None:
                res.append(node.data)
                sumSoFar -= node.data
            if sumSoFar == target:
                return sumSoFar
            curr = node.right

print("\nFor sum calculation\n")
ob2 = Solution2()
root2 = make_tree([10,5,15,2,7,20])
print(ob2.InorderTraversal(root2, 10))

def hasPathSum(node, s):
 
    # Return true if we run out of tree and s = 0
    if node is None:
        return (s == 0)
 
    else:
        ans = 0
 
        subSum = s - node.data
 
        # If we reach a leaf node and sum becomes 0, then
        # return True
        if(subSum == 0 and node.left == None and node.right == None):
            return True
 
        # Otherwise check both subtrees
        if node.left is not None:
            ans = ans or hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or hasPathSum(node.right, subSum)
 
        return ans

print(hasPathSum(root, 15))