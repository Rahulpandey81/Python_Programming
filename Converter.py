a=float(input("Enter The Feet to Convert"))
print("Select your option")
print("\n 1:- Feet to inches \n 2:- Feet to Yards \n 3:- Feet to miles \n 4:- Feet to Melemeters \n 5:- Feet to Centemeters \n 6:- Feet to meters \n 7:- Feet to kelemeters")
n=int(input("Select Your Option"))
if n==1:
    a=a*12
    print(a,"Inches")
elif n==2:
    a=a*0.33333
    print(a,"Yards")
elif n==3:
    a=a*0.00018939
    print(a,"miles")
elif n==4:
    a=a*304.8
    print(n,"feet=",a,"mm")
elif n==5:
    a=a*30.48
    print(a,"cm")
elif n==6:
    a=a*0.3048
    print(a,"Meters")
elif n==7:
    a=a*0.0003048
    print(a,"Km")
   

    
