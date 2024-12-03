import re
with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/dayThree/input.txt', 'r', encoding='utf-8') as file:
    # Zeilenweise lesen
    dataString = file.read()
    #flags=re.DOTALL über alle new lines sonst hört am ende der line mit re.sub check auf 
    dataString = re.sub(r"don't\(\).*?(?:do\(\)|$)", '', dataString, flags=re.DOTALL) 
    #. matched alle zeichen * beliebig oft ? - alle dazwischen werden betrachtet, $ da don't auch bis ans ende gehen kann und nicht mit do() endet
    pattern = r"mul\((\d+),(\d+)\)" #pattern für regex-muster im format (int,int)
    cleanedDataString = re.findall(pattern, dataString) #format 'int', 'int', ...
    sum = 0
    for data in cleanedDataString: 
        sum += int(data[0]) * int(data[1])
    
    print(sum)