import re
import time
from collections import Counter
n=input("Enter The Name of file that you wants to Count ")
fl=n+'.txt'
start = time.time()
words = 0
f=open(fl,'r').read().lower()
f1=open('dictionary','r').read().split("\n")

sb = re.sub("[a-z]*\d[a-z]*"," ",f)
fnd = re.findall("[a-z]+\'*[a-z]*\'*[a-z]*",sb)  
print("Total words in the file are ",len(fnd))
wc=Counter(fnd)
miss=(set(fnd).difference(set(f1)))
for line in miss:
    words +=wc[line]
print("Total miss spelled words are",words)
#fnd1=set(fnd)
#print("Total Distinct Words",len(fnd1))

end = time.time()
print("Total Time is used to comapre wordlist",end - start)

