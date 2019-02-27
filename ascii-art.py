l = int(input())
h = int(input())
t = input()

for i in range(h):
    row = input()
    pint=''
    for letter in t:
        letter = letter.upper()
        if ord(letter)-64 < 1 or ord(letter)-64 > 26 : letter = 26
        else :letter = int(ord(letter))-65
        for aff in range(l):
            pint += row[(letter*l)+aff]
    print(pint)  

