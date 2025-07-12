#return the missing number from a list of n consecutive numbers
n=int(input())

def sum_dig(n):
    sum=0
    for i in range (n+1):
        sum=sum+i
    return sum

nos=list(map(int, input().split()))
add=0
for i in nos:
    add=add+i

print(sum_dig(n)-add)    
