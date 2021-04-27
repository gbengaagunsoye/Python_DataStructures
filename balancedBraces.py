#This two here are my models
openBraces = ["[","{","("]
closeBraces = ["]","}",")"]

def balance(myStr):
    stack= []
    for i in myStr:
        if i in openBraces:
            #Here, I am pushing the braces in if it is an open brace
            # Remember if it starts with closed brace, it should automatically fail right    
            stack.append(i)
        elif i in closeBraces:
            #here if I meet a closed brace, I check what type of closed brace it is from my model by getting its index
            position = closeBraces.index(i)
            if ((len(stack) > 0) and (openBraces[position] == stack[len(stack)-1])): #here it must not be a closed brace when my stack is empty
                stack.pop()                                                    #and it must match the last element pushed into the stack, if it
                                                                        #does, I pop the stack, hence, deleting two matching braces.
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced" #end of function


print(balance("{[()](){}}"))
data = "[{]}"
print(balance(data))


version = ["1.0.4.5", "1.0.1.23", "2.1.3", "1.1.2.1"]
print(list(map(int, version[0].split("."))))
version.sort(key=lambda x:list(map(int, x.split("."))))
print(version)

import csv
import pandas as pd
filename = "C:\\Users\\amahm\\Documents\\Fall2020\\PROJECT\\53019_100708_bundle_archive\\Network-Traffic-Classification-master\\X_test.csv"
myfile = csv.reader(filename)
count = 0
for word in myfile:
    # if count == 10:
    #     break
    print(word)
    # count+=1
df = pd.read_csv(filename)
print(df.columns)

def matchBraces(text):
    stack = []
    for i in range(len(text)):
        if text[i] in openBraces:
            stack.append(text[i])
        elif stack:
            temp = stack.pop()
            pos = openBraces.index(temp)
            if closeBraces[pos] != text[i]:
                return False
    if stack:
        return False
    return True

print(matchBraces("{[()](){}}"))
data = "((((((((((((((((()"
print(matchBraces(data))