# def commonChild(s1, s2):
#     m = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
#     for i,c in enumerate(s1,1):
#         for j,d in enumerate(s2,1):
#             if c == d:
#                 m[i][j] = m[i-1][j-1]+1
#             else:
#                 m[i][j] = max(m[i][j-1],m[i-1][j])
                   
#     print(m)
#     return m[-1][-1]


# a = "HARRY"
# b = "SALLY"

# print(commonChild(a,b))



class HashTable():
    def __init__(self):
        self.max = 100
        self.arr = [None for x in range(self.max)]
    
    def getHash(self, key):
        h = 0
        for x in key:
            h+= ord(x)
        return h%self.max
    
    def __setitem__(self, key, value):
        index = self.getHash(key)
        self.arr[index] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        try:
            return self.arr[h]
        except:
            msg = "Key does not exist"
            return msg


t1 = HashTable()
t1["march 9"] = 20
print(t1["march 10"])
