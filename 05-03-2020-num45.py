# With U[1, 5] generate U[1, 7] of integers.

import random as rd

def rand5():
    return rd.randint(1, 5)

def rand7():
    found = False
    while not(found):
        found = True
        x1, x2 = rand5(), rand5()
        if x1 == 1:
            if x2 <= 3:
                return 1
            else: return 2
        if x1 == 2:
            if x2 == 1: return 2
            elif x2 <= 4: return 3
            else: return 4
        if x1 == 3:
            if x2 <= 2: return 4
            else: return 5
        if x1 == 4:
            if x2 <= 3: return 6
            else: return 7
        if x1 == 5:
            if x2 == 1: return 7
            else: found = False

print(rand7())

