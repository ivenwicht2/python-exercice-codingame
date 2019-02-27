import sys
from math import ceil

w, h = [int(i) for i in input().split()]
n = int(input())  
x0, y0 = [int(i) for i in input().split()]
minix = 0
miniy = 0
while True:
    di = input()
    for bdir in di :
        if bdir == 'U':
            mem = y0
            y0 = ceil(miniy + (h-y0)/2)
            h = mem
        if bdir == 'D':
            miniy = y0
            y0 = ceil(miniy +((h-y0)/2 ))
        if bdir == 'L':
            mem = x0
            x0 = ceil(minix + (w-x0)/2)
            w = mem
        if bdir == 'R' :
            minix = x0
            x0 = ceil(minix + ((w-x0)/2 ))
    if x0 > w : x0=w
    if y0 > h : y0=h
    if x0 < minix : x0 = minix
    if y0 < miniy : y0 = miniy
    print(x0,y0)
