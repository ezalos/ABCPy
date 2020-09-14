#!/usr/bin/env python

solution=[]
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        solution.append(str(i))

print('.'.join(solution))

print("Nb elem: ", len(solution))
