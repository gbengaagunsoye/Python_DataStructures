# /*
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


# ans = 2
# temp = 1+1
#        i
#  [1,1,1]

# iterate through list
# check if value at index is equal k, add 1 to contigous
# else 
# check if value at i+j = target
# add 1 to contigous
# set start point to j

# #[1,1,1]
#       i
#         j
# cont = 0, 1, 2
# temp = 1, 0, 1

# #[1 2 3]  k = 3
#   i
#     j
# cont = 0
# temp = 2, 3 

# */


# def countContiguous(nums, k):
#   n = len(nums)
#   ans = 0
#   if not nums:
#     return ans
#   if n ==1:
#     if nums[0] == k:
#       return ans+1
#     else:
#       return ans
#   cont = 0
#   temp = 0
#   i, j = 0, 1
#   while j < n:
#     if nums[i] == k:
#       cont+=1
#       i+=1
#       j+=1
#     else:
#       temp += nums[i]
#       if k - temp == nums[j]:
#         cont+=1
#         temp = 0
#         i = j
#         j = i+1
#       else:
#         i=j
#         j+=1
#   if nums[j] == k:
#     cont+=1
#   ans = cont
#   return ans

# nums = [1,2,3,5,6]
# k = 3
# print(countContiguous(nums, k))

def contiguous(num, k):
    res = 0
    sumSoFar = 0
    n = len(num)
    for i in range(n):
        for j in range(i, n):
            sumSoFar += num[j]
            print(sumSoFar)
            if sumSoFar == k:
                res+=1
        sumSoFar = 0
    return res

nums = [1,2,3,5,6]
k = 3
# nums = [1,1,1]
# k = 2
print(contiguous(nums, k))