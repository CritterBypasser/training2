N=str(input())
from collections import Counter
c=Counter(N)
Oddchar=0

for i in c.values():
        if i%2==1:
            Oddchar+=1
            
if Oddchar>1:
    print(False)
else:
    print(True)
    