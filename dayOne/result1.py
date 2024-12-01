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

with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/dayOne/numberList1.txt', 'r', encoding='utf-8') as file:
    data = file.read()

numbers = list(map(int, data.strip().split()))

listA = []
listB = []

for i in range(0, len(numbers)):
    if i % 2 == 0:
        listA.append(int(numbers[i]))
    else: listB.append(int(numbers[i]))
    
#bruteforce for part two

similarityScore = 0
count = 0
for i in range(0, len(listA)):
    for j in range(0, len(listB)):
        if listA[i] == listB[j]:
            count+=1
    similarityScore += listA[i]*count
    count = 0

#just for debugging (being able to compare text document to lists if correctly sorted)
print(listA) 
print("\n")
print(listB)
    
total_Distance = getDistance(sortList(listA), sortList(listB))
print("The total distance equals: ", total_Distance)

print("The similarity score is: ", similarityScore)