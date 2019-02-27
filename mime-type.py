doc={}
n = int(input())  
q = int(input())  
for i in range(n):

    ext, mt = input().split()
    doc[ext.upper()] = mt

for i in range(q):
    fname = input()  
    if fname.find('.') == -1 : result = "UNKNOWN"
    else :
        result =''
        mime = fname.split('.')
        for M in mime:
            if M.upper() in doc : result = doc[M.upper()]
            else : result = "UNKNOWN"
    print(result)

