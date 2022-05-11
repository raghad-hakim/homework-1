temp=list()
De=input('enter number')
binary=""
if De.isdigit():
    d=int(De)
    while d>0:
        temp.append(d%2)
        d//=2
    temp.reverse()
    for i in temp:
        binary+=str(i)
    print(binary)
else:
    print("error input")
