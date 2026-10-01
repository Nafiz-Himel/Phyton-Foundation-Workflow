strs = input()
numA = 0; numB = 0
for str in strs:
    if str == "A":
        numA += 1
    elif str == "B":
        numB += 1
numA = (numA/(numA+numB))*100
numB = (numB/(numA+numB))*100

if numA > 70 or numB > 70:
    print("Biased Model")
else:
    print("Fair Model")