import numpy as np
matrix1=np.matrix(
    [['X',1,2,4],
    [5,6,3,8],
    [9,10,7,12],
    [13,14,11,15]])
print(matrix1)
def start():
    ch=input("Enter the value to change the position 1 5->")
    if ch=='1':
        matrix1[0,1],matrix1[0,0]=matrix1[0,0],matrix1[0,1]
        print(matrix1)
        def substart():
            ch=input("Enter the value to change the position 1 2 6->")
            if ch=='1':
                matrix1[0,0],matrix1[0,1]=matrix1[0,1],matrix1[0,0]
                print(matrix1)
                start()
            elif ch=='2':
                matrix1[0,1],matrix1[0,2]=matrix1[0,2],matrix1[0,1]
                print(matrix1)
                def sub2():
                    ch=input("Enter the value to change the position 2 3 4->")
                    if ch=='2':
                        matrix1[0,1],matrix1[0,2]=matrix1[0,2],matrix1[0,1]
                        print(matrix1)
                        substart()
                    elif ch=='4':
                        matrix1[0,3],matrix1[0,2]=matrix1[0,2],matrix1[0,3]
                        print(matrix1)
                        def sub4():
                            ch=input("Enter the value to change the position 4 8->")
                            if ch=='4':
                                matrix1[0,3],matrix1[0,2]=matrix1[0,2],matrix1[0,3]
                                print(matrix1)
                                sub2()
                            elif ch=='8':
                                matrix1[0,3],matrix1[1,3]=matrix1[1,3],matrix1[0,3]
                                print(matrix1)
                                def sub8():
                                    ch=input("Enter the Value to change the position 3 8 12->")
                                    if ch=='3':
                                        matrix1[1,2],matrix1[1,3]=matrix1[1,3],matrix1[1,2]
                                        print(matrix1)
                                    elif ch=='8':
                                        matrix1[0,3],matrix1[1,3]=matrix1[1,3],matrix1[0,3]
                                        print(matrix1)
                                        sub4()
                                sub8()
                        sub4()

                    elif ch=='3':
                        matrix1[0,2],matrix1[1,2]=matrix1[1,2],matrix1[0,2]
                        print(matrix1)
                        def sub3():
                            ch=input("Enter the value to change the position 3 6 7 8->")
                            if ch=='3':
                                matrix1[0,2],matrix1[1,2]=matrix1[1,2],matrix1[0,2]
                                print(matrix1)
                                sub2()
                            elif ch=='6':
                                matrix1[1,1],matrix1[1,2]=matrix1[1,2],matrix1[1,1]
                                print(matrix1)
                            elif ch=='8':
                                matrix1[1,2],matrix1[1,3]=matrix1[1,3],matrix1[1,2]
                                print(matrix1)
                            elif ch=='7':
                                matrix1[1,2],matrix1[2,2]=matrix1[2,2],matrix1[1,2]
                                print(matrix1)
                                def sub7():
                                    ch=input("Enter the value to change the position 10 7 11 12->")
                                    if ch=='11':
                                        matrix1[2,2],matrix1[3,2]=matrix1[3,2],matrix1[2,2]
                                        print(matrix1)
                                        def sub11():
                                            ch=input("Enter the value to change the position 14 11 15->")
                                            if ch=='15':
                                                matrix1[3,2],matrix1[3,3]=matrix1[3,3],matrix1[3,2]
                                                print(matrix1)
                                                print("Congratulation you won the Game!!!!")
                                        sub11()
                                sub7()

                                
                                
                        sub3()
                sub2()
            elif ch=='6':
                matrix1[0,1],matrix1[0,0]=matrix1[0,0],matrix1[0,1]
                print(matrix1)
        substart()
        
    elif ch=='5':
        matrix1[1,0],matrix1[0,0]=matrix1[0,0],matrix1[1,0]
        print(matrix1)
        def sub5():
            ch=input("Enter tye value to change the position 5 6 9->")
            if ch=='5':
                matrix1[1,0],matrix1[0,0]=matrix1[0,0],matrix1[1,0]
                print(matrix1)
                start()
            elif ch=='6':
                matrix1[1,0],matrix1[1,1]=matrix1[1,1],matrix1[1,0]
                print(matrix1)
                def sub6():
                    ch=input("Enter the value to change the position 6 1 3 10->")
                    if ch=='6':
                        matrix1[1,0],matrix1[1,1]=matrix1[1,1],matrix1[1,0]
                        print(matrix1)
                        sub5()
                    elif ch=='1':
                        matrix1[0,1],matrix1[1,1]=matrix1[1,1],matrix1[0,1]
                        print(matrix1)
                    elif ch=='3':
                        matrix1[1,1],matrix1[1,2]=matrix1[1,2],matrix1[1,1]
                        print(matrix1)
                    elif ch=='10':
                        matrix1[1,1],matrix1[2,1]=matrix1[2,1],matrix1[1,1]
                        print(matrix1)
                sub6()
            elif ch=='9':
                matrix1[2,0],matrix1[1,0]=matrix1[1,0],matrix1[2,0]
                print(matrix1)
                def sub9():
                    ch=input("Enter The vlaue to change the position 9 13 10->")
                    if ch=='13':
                        matrix1[2,0],matrix1[3,0]=matrix1[3,0],matrix1[2,0]
                        print(matrix1)
                    elif ch=='10':
                        matrix1[2,0],matrix1[2,1]=matrix1[2,1],matrix1[2,0]
                        print(matrix1)
                    elif ch=='9':
                        matrix1[2,0],matrix1[1,0]=matrix1[1,0],matrix1[2,0]
                        print(matrix1)
                        sub5()
                sub9()
        sub5()
        
    else:
        print("Please enter valid Position to move")
  
    
        
    
start()
