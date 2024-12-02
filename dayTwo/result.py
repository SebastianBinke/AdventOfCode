safeReports = 0
monotone = []

with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/dayTwo/input.txt', 'r', encoding='utf-8') as file:
    # zeilenweise lesen, read wäre als gesamtes 
    data = file.readlines()

# every line to subarray
reports = [list(map(int, line.split())) for line in data if line.strip()]

# monotone Subarrays
for subarray in reports:
    # Prüfen, ob das Subarray mindestens zwei Elemente enthält
    if len(subarray) > 1:
        # streng monoton steigend
        is_increasing = all(x < y for x, y in zip(subarray, subarray[1:]))
        # streng monoton fallend
        is_decreasing = all(x > y for x, y in zip(subarray, subarray[1:]))
        if is_increasing or is_decreasing:
            monotone.append(subarray)
    else:
        pass

# Überprüfe Differenzbedingungen für monotone Subarrays
for subarray in monotone:
    count = 0 
    for j in range(len(subarray) - 1):
        diff = abs(subarray[j] - subarray[j + 1])
        if 1 <= diff <= 3:
            count += 1
    # Wenn alle Differenzen die Bedingung erfüllen
    if count == len(subarray) - 1:
        safeReports += 1

# Debug
print("Monotone Subarrays:", monotone)
print("Die Anzahl beträgt:", safeReports)
