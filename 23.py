#!/bin/python
#non-abundant numbers


def factor(number):
    lst = [1]
    c = 2
    temp = number
    while c < temp:
        if number % c == 0:
            lst.append(c)
            temp = number // c
            if temp > c:
                lst.append(temp)
        c += 1
    return sum(lst)



abundants = []
n = []
for i in range(1,28124):
    n.append(i)
    if i < factor(i):
        abundants.append(i)

for first in abundants:
    print(first)
    for second in abundants:
        total = first + second
        if total in n:
            n.remove(total)
    abundants.remove(first)

print(sum(n))
