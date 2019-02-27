import sys
import math

width = int(input()) 
height = int(input()) 


tableau = [[ "3" for i in range(width)]for i in range(height)]
for i in range(height):
    line = input()
    for j in range(width):
        tableau[i][j]=line[j]

for i in range(height):
    for j in range(width):
        
        if tableau[i][j] == '0' :
            
            print(j,i,end=" ")
            
            found = "-1 -1"
            if j == width-1 : print("-1 -1",end=" ")
            else :
                for x in range(1,width-j):
                    if tableau[i][j+x] == '0' : 
                        found =  str(j+x)+ ' ' + str(i)
                        break;
                print(found,end=" ")
        
        
            found = "-1 -1"
        
            if i == height-1 : print("-1 -1")
            else : 
                for y in range(1,height-i):
                    if tableau[i+y][j] == '0': 
                        found = str(j) + ' ' + str(i+y)
                        break;
                print(found)
        

