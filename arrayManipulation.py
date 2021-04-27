
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    myArray = []
    for query in queries:
        myArraySize = len(myArray)
        # tracker = len(query)
        # value = query[(tracker-1)]
        value = query[2]
        # print(value)
        start = max(query[0],0)
        # print(start)
        end = query[1]
        # print(end)
        # start = query[0]-1
        # if(start >= myArraySize):
        #     print("Start Greater than Array")
        #     instantArray = [0] * (start - myArraySize)
        #     myArray = myArray + instantArray
        #     print("New Expansion Array")
        #     print(myArray)
        if(start == end and start >= myArraySize):
            print("Start and End are Same and we need  to expand")
            instantArray = [0] * (start - myArraySize)
            myArray = myArray + instantArray
            myArray[start-1] = myArray[start-1] + value
            continue
        else:
            if(start == end and start < myArraySize):
                print("Start and End are Same but no expansion")
                print(start)
                # print(end)
                # start = start - 1
                myArray[start-1] = myArray[start-1] + value
                continue
            else:
                if(end > myArraySize):
                    # print("End Greater than Array")
                    instantArray = [0] * (end - myArraySize)
                    myArray = myArray + instantArray
                    # print("New Expansion Array below:")
                    # print(myArray)
                    # print(start)  
                for x in range(start-1, end):
                    myArray[x] = myArray[x] + value
        #print(myArray)    
    return max(myArray)


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    myArray = []
    for query in queries:
        myArraySize = len(myArray)
        # tracker = len(query)
        # value = query[(tracker-1)]
        value = query[2]
        # print(value)
        start = max(query[0],0)
        # print(start)
        end = query[1]
        # print(end)
        # start = query[0]-1
        # if(start >= myArraySize):
        #     print("Start Greater than Array")
        #     instantArray = [0] * (start - myArraySize)
        #     myArray = myArray + instantArray
        #     print("New Expansion Array")
        #     print(myArray)
        if(start == end and start >= myArraySize):
            print("Start and End are Same and we need  to expand")
            instantArray = [0] * (start - myArraySize)
            myArray += instantArray
            myArray[start-1] += value
            continue
        else:
            if(start == end and start < myArraySize):
                print("Start and End are Same but no expansion")
                print(start)
                # print(end)
                # start = start - 1
                myArray[start-1] += value
                continue
            else:
                if(end > myArraySize):
                    # print("End Greater than Array")
                    instantArray = [0] * (end - myArraySize)
                    myArray += instantArray
                    # print("New Expansion Array below:")
                    # print(myArray)
                    # print(start)  
                for x in range(start-1, end):
                    myArray[x] += value
        # print(myArray)    
    return max(myArray)
