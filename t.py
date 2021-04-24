#!/usr/bin/env python

l = list('1234567890qwertyuiopasdfght')
#  print(*l)

dl = []
itmes_by_list = 10
for i, v in enumerate(l):
    #  print(i, i//5, i%5, v)
    if i%itmes_by_list == 0:
        dl.append([])
    dl[i//itmes_by_list].append(v)

print(*dl)
