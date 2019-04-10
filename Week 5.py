import urllib
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print ("Count : ",count)
print ("Sum : ",sum)

"""Output:Enter -   http://py4e-data.dr-chuck.net/comments_187845.xml

Count :  50
Sum :  2468
"""
