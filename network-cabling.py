import sys
n = int(input())
median = 0
total = 0
liste=[]
chemin = []
if n%2 != 0 : median = (n+1)/2
else : median = n/2

for i in range(n):
    x , y = [int(j) for j in input().split()]
    liste.append(y)
    chemin.append(x)
liste.sort()

for i in range(n):
    total += abs(liste[i]-liste[int(median)-1])

chemin = set(chemin)
chemin2 = []
for i in chemin:
    chemin2.append(i)
chemin2.sort()

totalC = 0
for i in range(len(chemin2)):
    if i !=0 : totalC += chemin2[i] - chemin2[i-1]
    
print(total+totalC)
