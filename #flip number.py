#flip number
n= int(input())
for i in range(n):
    flag=0
    for ch in str(i):
        if ch==1 or ch==6 or ch==8 or ch==9:
            flag+=1
        else:
            flag=0
            break
    if flag >0:
        print(i)

