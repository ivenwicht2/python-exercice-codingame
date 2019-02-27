w, h = [int(i) for i in input().split()]
save = [ input() for i in range(h)]
entrer = [i for i in save[0].split('  ')]

rg = len(entrer)

for i in range(rg):
    print(entrer[i],end='')
    x,y = i*3,1
    while y < h:
        ok = 0
        if x < w-1 :
            if save[y][x+1] == '-' :
                x += 3
                ok = 1
        if x > 0 :
            if save[y][x-1] == '-' and ok == 0 :
                x -= 3    
        y+=1
    print(save[y-1][x])
