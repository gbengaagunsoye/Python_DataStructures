def find_busiest_period(data):
    currentTimeStamp = 0
    timestampTotal = 0
    total = 0
    tempMinimumTimestamp = 0
    n = len(data)
    if n == 1:
      return data[0][0]
    i = 0
    while i < n:
        if data[i][0] == currentTimeStamp:
            total = total + data[i][1] if data[i][2] == 1 else  total - data[i][1]
            i+=1
        else:
            if total > timestampTotal:
                timestampTotal = total
                tempMinimumTimestamp = currentTimeStamp
            currentTimeStamp = data[i][0]
            total = 0
    # print(i, currentTimeStamp)
    if total > timestampTotal:
        timestampTotal = total
        tempMinimumTimestamp = currentTimeStamp       
    return tempMinimumTimestamp
  
#pass # your code goes here

data = [[1487799425,14,1],
        [1487799425,4,1],
        [1487799425,2,1],
        [1487800378,10,1],
        [1487801478,38,1],
        [1487901013,1,1],
        [1487901211,7,1],
        [1487901211,7,1]]
print(find_busiest_period(data))


from collections import Counter
def find_busiest_period(data):
  c = Counter()
  for [t,n,v] in data:
    if v == 1: c[t] += n
    else: c[t] -= n
  return c.most_common(1)[0][0]
  