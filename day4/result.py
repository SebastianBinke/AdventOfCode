with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/day4/input.txt', 'r', encoding='utf-8') as file:
    dataSet = (file.read())
    
    listForEveryRow = [list(line.strip()) for line in dataSet.splitlines() if line.strip()]
    #forward
    sum = 0
    #horizontal 
    for i in range(len(listForEveryRow)): #funktioniert
        for j in range(len(listForEveryRow[i])-3):
            if listForEveryRow[i][j] == 'X' and listForEveryRow[i][j+1] == 'M' and listForEveryRow[i][j+2] == 'A' and listForEveryRow[i][j+3] == 'S':
                sum += 1
            #reverse 
            if listForEveryRow[i][j] == 'S' and listForEveryRow[i][j + 1] == 'A' and listForEveryRow[i][j + 2] == 'M' and listForEveryRow[i][j + 3] == 'X':
                sum += 1
    #vertical
    for i in range(len(listForEveryRow)-3): #funktioniert 
        for j in range(len(listForEveryRow[i])):    
            if listForEveryRow[i][j] == 'X' and listForEveryRow[i+1][j] == 'M' and listForEveryRow[i+2][j] == 'A' and listForEveryRow[i+3][j] == 'S':
                sum += 1
            #reverse
            if listForEveryRow[i][j] == 'S' and listForEveryRow[i+1][j] == 'A' and listForEveryRow[i+2][j] == 'M' and listForEveryRow[i+3][j] == 'X':
                sum += 1
    #diagonal left to right  
    for i in range(len(listForEveryRow)-3): #funktioniert
        for j in range(len(listForEveryRow[i])-3):
            if listForEveryRow[i][j] == 'X' and listForEveryRow[i+1][j+1] == 'M' and listForEveryRow[i+2][j+2] == 'A' and listForEveryRow[i+3][j+3] == 'S':
                sum += 1
            #reverse
            if listForEveryRow[i][j] == 'S' and listForEveryRow[i+1][j+1] == 'A' and listForEveryRow[i+2][j+2] == 'M' and listForEveryRow[i+3][j+3] == 'X':
                sum += 1
    #diagonal right to left
    for i in range(len(listForEveryRow) - 3):  #funktioniert 
        for j in range(3, len(listForEveryRow[i])):  
            if listForEveryRow[i][j] == 'X' and listForEveryRow[i+1][j-1] == 'M' and listForEveryRow[i+2][j-2] == 'A' and listForEveryRow[i+3][j-3] == 'S':
                sum += 1
            # Reverse
            if listForEveryRow[i][j] == 'S' and listForEveryRow[i+1][j-1] == 'A' and listForEveryRow[i+2][j-2] == 'M' and listForEveryRow[i+3][j-3] == 'X':
                sum += 1
    
    # part2 
    secondSum = 0
    for i in range(1, len(listForEveryRow)-1):
        for j in range(1, len(listForEveryRow[i])-1):
            if listForEveryRow[i][j] == 'A':
                if (listForEveryRow[i-1][j-1] == 'M' and listForEveryRow[i-1][j+1] == 'M' and
                    listForEveryRow[i+1][j-1] == 'S' and listForEveryRow[i+1][j+1] == 'S'):
                    secondSum += 1
                    print(i,j)
                if (listForEveryRow[i-1][j-1] == 'S' and listForEveryRow[i-1][j+1] == 'S' and
                    listForEveryRow[i+1][j-1] == 'M' and listForEveryRow[i+1][j+1] == 'M'):
                    secondSum += 1
                    print(i,j)
                if (listForEveryRow[i-1][j-1] == 'M' and listForEveryRow[i-1][j+1] == 'S' and
                    listForEveryRow[i+1][j-1] == 'M' and listForEveryRow[i+1][j+1] == 'S'):
                    secondSum += 1
                    print(i,j)
                if (listForEveryRow[i-1][j-1] == 'S' and listForEveryRow[i-1][j+1] == 'M' and
                    listForEveryRow[i+1][j-1] == 'S' and listForEveryRow[i+1][j+1] == 'M'):
                    secondSum += 1
                    print(i,j)
                
    #debug
    print("Part 1: ", sum)
    print("Part 2: ", secondSum)
    