import math
f=0
n=0
for i in range(1,101):
    h=i**2
    m=str(h)
    if m[-1]=='4':
        
        print(h)
        f=f+1
    elif m[-1]=='9':
        print(h)
        n=n+1
print("Total 4 in the end =",f)
print("Total Nine In the end=",n)





