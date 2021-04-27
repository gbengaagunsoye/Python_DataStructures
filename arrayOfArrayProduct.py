import time
def array_of_array_products(arr):
    output = []
    n = len(arr)
    if n==1:
        return []
    # product  = 1
    for i in range(n):
        product  = 1
        j = 0
        while j < n:
            if j==i:
                pass
            else:
                product = product * arr[j]
            j+=1
        output.append(product)    
        
    return output
arr = [8, 10, 2]
t = time.time()
print(array_of_array_products(arr))
print(time.time() - t)

def array_of_array_product(arr):
    n = len(arr)
    if n == 1:
        return []
    output1 = [0] * n
    left = 1
    preproceesor = [1] * n
    for i in range(n-2,-1,-1):
        preproceesor[i] = preproceesor[i+1] * arr[i + 1]
        #[20,2,1]
        
    for i in range(n):
        j = 0
        right = preproceesor[i]
        output1[i] = left * right
        #[20,16,80]
        left = left * arr[i]
        
    return output1

arr = [8, 10, 2]
t = time.time()
print(array_of_array_product(arr))
print(time.time() - t)