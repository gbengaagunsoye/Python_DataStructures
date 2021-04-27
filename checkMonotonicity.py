
def checkMonotonicity(arr):
    size = len(arr)-2
    newList = [0] * size
    newList2 = [0] * size
    for x in range(len(arr)-2):
        nextIndex = x+1
        if arr[x] <= arr[x+1]:
            newList[x] = 1
    
    for x in range(len(arr)-2):
        nextIndex = x+1
        if arr[x] >= arr[x+1]:
            newList2[x] = 1

    return newList, newList2
    


def checkMonotoneIncreasing(arr):
    return (all(arr[index] <= arr[index+1] for index in range(len(arr)-1)))

def checkMonotoneDecreasing(arr):
    return (all(arr[index] >= arr[index+1] for index in range(len(arr)-1)))
    # myList = [1 for index in range(len(arr)-1) if all(arr[index] <= arr[index+1])]
    # for index in range(len(arr)-1):
    #     myDict.setdefault(integer, 0)
    #     if

# print(checkMonotoneIncreasing([1,2,3,3,4,5]))
# print(checkMonotonicity([8,7,3,3,4,5]))
# print(sorted(str("1,2,3,3,4,5")))
# print(checkMonotonicity(sorted(str([1,2,3,3,4,5]), key=reversed)))



def primeNumbers(number):
    prime = [True for x in range(number+1)]
    firstPrime = 2
    while(firstPrime**2 <= number):
        if prime[firstPrime] == True:
            for x in range(firstPrime**2, number+1, firstPrime):
                prime[x] = False
        firstPrime+=1
    
    res = [x for x in range(2, number+1) if prime[x]]
    print(res)


primeNumbers(10)