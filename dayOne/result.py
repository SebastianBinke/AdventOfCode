def swap(givenList, i, j): 
    temp = givenList[i]
    givenList[i] = givenList[j]
    givenList[j] = temp
    return givenList

def sortList(givenList):
    for i in range(len(givenList) - 1):  
        for j in range(i + 1, len(givenList)):  
            if givenList[j] < givenList[i]:
                swap(givenList, i, j)
    return givenList

def getDistance(ListA, ListB): 
    total_distance = 0
    for i in range(len(ListA)):
        total_distance += abs(ListA[i] - ListB[i])  
    return total_distance 

with open('numberList1.txt', 'r', encoding='utf-8') as file:
    data = file.read()

numbers = list(map(int, data.strip().split()))

listA = []
listB = []

for i in range(0, len(numbers)):
    if i % 2 == 0:
        listA.append(int(numbers[i]))
    else: listB.append(int(numbers[i]))

print(listA)
print("\n")
print(listB)
    
total_Distance = getDistance(sortList(listA), sortList(listB))
print("Die totale Distanz beträgt: ", total_Distance)
