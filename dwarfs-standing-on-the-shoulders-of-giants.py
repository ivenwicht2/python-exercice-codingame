dic = {}

def arbre(number):
    global dic
    maxi = 0
    array = dic.get(number,[])
    if array == 0 :
        return 0
    else:
        for item in array:
            temp = arbre(item)
            if temp > maxi :
                maxi = temp
        return maxi + 1 
            
n = int(input()) 
for i in range(n):
 
    x, y = [int(j) for j in input().split()]
    dic.setdefault(x,[]).append(y)
    
maxi = 0
for item in dic:
    temp = arbre(item)
    if temp > maxi :
        maxi = temp
print(maxi)
