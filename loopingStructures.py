import random
loopList = ["hello", 1, 2, 3,"ABC",123.456]
for i in range(len(loopList)):
    print(loopList[i])

randomList = []
for i in range(50):
    randomList.append(random.randint(0,1000))

print(randomList)