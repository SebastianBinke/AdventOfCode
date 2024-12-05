
def formatInput(input): # set of rules pre and post from input 
  pairs = set((pre,post) for pre, post in 
                      [map(int, line.strip().split('|')) for line in input if '|' in line])
  updates = [list(map(int, line.strip().split(','))) for line in input if ',' in line] # updates 
  return pairs, updates

def findCorrect(updates):
  return [u for u in updates if u == correctUpdate(u)]

def findIncorrect(updates):
  return [u for u in updates if u != correctUpdate(u)]

def correctUpdate(u):
  return sorted(u, key=lambda x: sum([(e,x) in pairs for e in u]))


with open('/Users/sebastianbinke/Documents/GitHub/AdventOfCode/day5/input.txt', 'r') as file:
    input = file.readlines()

pairs, updates = formatInput(input)

print('Part1: ', sum([u[len(u)//2] for u in findCorrect(updates)]))
print('Part2: ', sum([u[len(u)//2] for u in map(correctUpdate, findIncorrect(updates))]))