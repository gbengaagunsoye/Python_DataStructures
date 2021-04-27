def find_largest_smaller_key(self, num):
    temp = [-1, 0]
    curr = self.root
    def searchKey(root, num, temp):
      if root is None:
        return temp[0]
      if root.key > num:
        #go Left
        searchKey(root.left, num, temp)
      else:
        #go right
        if temp[0] == -1:
          temp = [root.key, num - root.key]
          searchKey(root.right, num, temp)
        else:
          if num - root.key < temp[1]:
            temp = [root.key, num - root.key]
            searchKey(root.right, num, temp)
    return searchKey(curr, num, temp)