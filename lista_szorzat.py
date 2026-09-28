n=int(input())
list=[]
while type(n) is int:
    list.append(n)
    n=int(input())
if len(list)==0:
    print("Az elemek szorzata 1.\nAz elemek összege 0.")
else:
    sum=0
    prod=1
    for j in range(len(list)):
        sum+=list[j]
        prod*=list[j]
    print("Az elemek szorzata "+prod+ "\nAz elemek összege "+sum)
