from collections import Counter

def reverseSentence(data):
    arr = data.split()
    newArr = arr[::-1]
    # for x in range(size):
    #     print(arr[size-x-1])
    return newArr


print(reverseSentence("Hello World, Today is Thursday"))
count = Counter(reverseSentence("Hello World, Today is Thursday"))
print(count)

myDict = {}
for x in (reverseSentence("Hello World, Today is Thursday")):
    if x in myDict.items():
        myDict[x]+= 1
    else:
        myDict.setdefault(x,1)
    # myDict.setdefault(x, 0)
    # myDict[x] += 1
print (myDict)
# y = [x for x in myDict.items()]
# print(y)