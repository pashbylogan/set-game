import json
import numpy as np
from itertools import combinations

number = [0,1,2]
color = [0,1,2]
pattern = [0,1,2]
shape = [0,1,2]
d = {}

combos = np.array(np.meshgrid(number, color, pattern, shape)).T.reshape(-1, 4)
s = set()

for item in combos:
    s.add(tuple(item))

d['cards'] = s

card_combos = list(combinations(s, 3))
sets = set()

def check_index(idx, t):
    nums = [t[0][idx], t[1][idx], t[2][idx]]
    l = len(set(nums))
    if l == 1 or l == 3:
        return True
    else:
        return False

def check(t):
    result = True
    for i in range(3):
        result = result and check_index(i, t)
    return result

for s in card_combos:
    print(s)
    if check(s):
        sets.add(s)

print(len(sets))
