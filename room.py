from collections import Counter
a=int(input())
n=list(map(int, input().split()))

c=Counter(n)
for room, count in c.items():
    if count!=a:
        print(room)
        break

