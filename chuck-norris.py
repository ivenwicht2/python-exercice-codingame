txt=''
binary=''
message = input()

for letter in message:
    binary+= str(bin(ord(letter)))[2:].zfill(7)

zoo = '-1'

for bin in binary:
    if zoo != '1' and bin == '1' :
        txt+=' 0 '
        zoo='1'
    elif zoo != '0' and bin =='0' : 
        txt+=' 00 '
        zoo='0'
    txt += '0'
print(txt.strip())


