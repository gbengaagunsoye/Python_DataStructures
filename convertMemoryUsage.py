import re
multipliers = {"K":10**3, "M":10**6, "G":10**9}
def convertUsage(data):
    newData = []
    for usage in data:
        usage = usage if usage else "0"
        groups =  re.match(r"(\d+\.\d+|\d+)(\D+)", usage)
        numericPart = groups.group(1) if groups != None else usage
        print(usage, numericPart)
        mulPart = groups.group(2) if groups != None else 1
        if mulPart in multipliers.keys():
            res = float(numericPart) * multipliers[mulPart]
            newData.append(res)
        elif numericPart and mulPart==1:
            newData.append(float(numericPart))
    return newData


memUsage = ["", "0", "1", "20.4K", "1M", "3GB", "4P"] + ['', '10', '10GK', '2.3K', '2.34K', '2M', '2.2M', '2.23M']

# convertedMemUsage = convertUsage(memUsage)
# print(convertedMemUsage)
print(convertUsage(["10GK"]))

def f(s):
    try:
        if s[-1] in multipliers.keys():
            return float(s[:-1]) * multipliers[s[-1]]
        else:
            return float(s)
    except:
        return s

print("Second part")
res = list(map(f, ['', '10', '10GK', '2.3K', '2.34K', '2M', '2.2M', '2.23M']))
res = [x for x in res if type(x) == float]
print(res)