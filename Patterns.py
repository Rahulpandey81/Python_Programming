'''1:-Pattern to print 1
                    2 2
                    3 3 3
                    4 4 4 4
                    5 5 5 5 5'''
for x in range(0,6):
    for y in range(0,x):
        print(x,end=" ")
    print("\n")


    

'''2:-Pattern to print 1
                    1 2
                    1 2 3
                    1 2 3 4
                    1 2 3 4 5'''
for x in range(1,7):
    for y in range(1,x):
        print(y,end=" ")
    print("\n")







'''3:-Pattern to print 1
                       2 3
                       4 5 6
                       7 8 9 10'''
a=1
for x in range(1,6):
    for y in range(1,x):
        print(a,end=" ")
        a=a+1
    print("\n")





'''4:-Pattern to print *
                       * *
                       * * *
                       * * * *
                       * * * * *'''
for x in range(1,6):
    for y in range(1,x):
        print("*",end=" ")
    print("\n")




    
    
'''5:-Pattern to print * * * * *
                       * * * *
                       * * *
                       * *
                       * '''
for x in range(1,6):
    for y in range(x,6):
        print("*",end=" ")
    print("\n")





'''6:-Pattern to print *        *
                        *      *
                         *   *
                           **
                           * *
                          *   *
                        *      *'''
for x in range(1,10):
    ptrn=list(" "*10)
    ptrn[x]="*"
    ptrn[-(x+1)]="*"
    print("".join(ptrn))




'''7:-Pattern to print  ***      *** 
                         ***    ***  
                          ***  ***   
                           ******    
                           ******    
                           ***  ***   
                          ***    ***  
                         ***      *** 
                        ***        *** '''
for x in range(1,10):
    ptrn=list(" "*10)
    ptrn[x]="*"*3
    ptrn[-(x+1)]="*"*3
    print("".join(ptrn))





'''8:-Pattern to print A
                    B B
                    C C C
                    D D D D
                    .........Z'''
a=65
for i in range(64,90):
    for j in range(63,i):
        c=chr(a)
        print(c,end=" ")
    a=a+1
    print("\n")

    

'''9:-Pattern of Leg'''
for i in range(1,25):
    print("*"*15)
for j in range(1,15):
    ptrn=list(" "*20)
    ptrn[j]="*"*15
    ptrn[-(j+1)]="*"*20
    print("".join(ptrn))
for k in range(1,10):
    a=("*"*30)
    print("@".join(a))
        
