def countBitSet(inputNum):
    bits = bin(int(inputNum)).lstrip("0b")
    hexa = hex(int(inputNum))
    octa = oct(inputNum)
    print(hexa, octa)
    return bits.count("1")

print(countBitSet("18"))

#output = 2