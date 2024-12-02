safeReports = 0

with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/dayTwo/input.txt', 'r', encoding='utf-8') as file:
    # Zeilenweise lesen
    data = file.readlines()

# Jede Zeile zu einem Subarray
reports = [list(map(int, line.split())) for line in data if line.strip()]

for subarray in reports:
    is_safe = False

    # check, Subarray bereits sicher
    if len(subarray) > 1:
        # check strenge monotonie
        is_increasing = all(x < y for x, y in zip(subarray, subarray[1:]))
        is_decreasing = all(x > y for x, y in zip(subarray, subarray[1:]))

        if is_increasing or is_decreasing:
            # Differenzbedingung
            if all(1 <= abs(x - y) <= 3 for x, y in zip(subarray, subarray[1:])):
                is_safe = True

    if not is_safe:
        # try to remove 1 element to make safe
        for i in range(len(subarray)):
            # create new subarray without i-th element
            new_subarray = subarray[:i] + subarray[i+1:] # slicing -> extrahiere teile des arrays
            # :i alle elemente bis i aber nicht i, i+1: alle elemente ab i+1 bis ende --> extrahiere i in dem ich beide listen verbinde
            if len(new_subarray) > 1:
                is_increasing = all(x < y for x, y in zip(new_subarray, new_subarray[1:]))
                is_decreasing = all(x > y for x, y in zip(new_subarray, new_subarray[1:]))

                if is_increasing or is_decreasing:
                    if all(1 <= abs(x - y) <= 3 for x, y in zip(new_subarray, new_subarray[1:])):
                        is_safe = True
                        break  # Kein weiteres Element entfernen

    if is_safe:
        safeReports += 1

print("Die Anzahl beträgt:", safeReports)
