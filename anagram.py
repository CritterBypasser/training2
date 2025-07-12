n=int(input())
def anag(str1,str2):
    count=0
    flag=0
    for ch in str1:
        count+=1
    for i in range (count):
        for ch1 in str1:
            for ch2 in str2:
                if ch1== ch2:
                    flag+=1
    print(count)
    print(flag)                
    if flag==count:
        return str1,str2
    else:
        return 0

k=list(map(str, input().split()))    
for i in range(len(k)):
    for j in range(len(k)):
        print(anag(k[i],k[j]))