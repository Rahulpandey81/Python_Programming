string=input("Enter string:").split(" ")
vowels=0
for i in string:
      if(i=='a'or i=="an" or i=="the" or i=="A" or i=="An" or i=="The"):
            vowels=vowels+1
print("Total Number of Article Used in this String are:-")
print(vowels)


a=[10,20,30]
b=(30,40,50)
c=list(zip(a,b))
print(c)
