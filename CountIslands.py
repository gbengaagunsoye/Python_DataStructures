from collections import deque

def adjacencyMatrix(binaryMatrix):
    row = len(binaryMatrix)
    col = len(binaryMatrix[0])
    adjacent = 0

    def pushifValid(stack, row, col, x, y):
        if (x>=0 and x<row and y >= 0 and y < col):
            stack.append([x,y])

    def findAdjacent(i, j):
        stack = deque()
        stack.append([i,j])
        while not stack:
            item = stack.popleft()
            x, y = item[0], item[1]
            if binaryMatrix[x][y] ==1:
                print("here")
                binaryMatrix[x][y] = -1
                pushifValid(stack, row, col, x-1, y)
                pushifValid(stack, row, col, x, y-1)
                pushifValid(stack, row, col, x+1, y)
                pushifValid(stack, row, col, x, y+1)

    

    for i in range(row):
        for j in range(col):
            if binaryMatrix[i][j] == 1:
                findAdjacent(i,j)
                adjacent+=1
    return adjacent


binaryMatrix = [ [0,    1,    0,    1,    0], [0,    0,    1,    1,    1], [1,    0,    0,    1,    0], [0,    1,    1,    0,    0], [1,    0,    1,    0,    1]]

print(adjacencyMatrix(binaryMatrix))
# print(binaryMatrix)