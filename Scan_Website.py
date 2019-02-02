import urllib.request
import sys
url=input("Enter the Name of website")
url.rstrip()
header=urllib.request.urlopen(url).info()
print (str(header))

