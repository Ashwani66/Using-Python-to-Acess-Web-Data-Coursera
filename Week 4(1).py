import urllib
from bs4 import BeautifulSoup
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print (s[position-1])
    print (t[position-1])
    url = s[position-1]


"""
Output:
Enter Url:   http://py4e-data.dr-chuck.net/known_by_Hassanali.html
Enter count:  7
Enter position: 18

http://py4e-data.dr-chuck.net/known_by_Sabila.html
Sabila
http://py4e-data.dr-chuck.net/known_by_Kristopher.html
Kristopher
http://py4e-data.dr-chuck.net/known_by_Ilsa.html
Ilsa
http://py4e-data.dr-chuck.net/known_by_Kyler.html
Kyler
http://py4e-data.dr-chuck.net/known_by_Reese.html
Reese
http://py4e-data.dr-chuck.net/known_by_Maaz.html
Maaz
http://py4e-data.dr-chuck.net/known_by_Lennox.html
Lennox
"""
