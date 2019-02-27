n = int(input())
cote = input().split(' ')

maxcote = 0
last = int(cote[0])
stock = 0
fall = 0
for num in cote :
    
    num = int(num)
    
    if num > maxcote : maxcote = num
    
    if last > num : stock = num - maxcote
    
    if stock < fall : fall = stock
    
    last = num
    
print(fall)
