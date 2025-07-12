#print all the prime numbers in a range from 1 to n

N=int(input('enter the number  ' ))

def isPrime(n):
    for k in range (2, n//2 +1):
        if n%k==0:
            return(False)
    return(True)
            
def checkNo(n):
    for i in range(2,N):
        if isPrime(i):
            print(i)
checkNo(N)


N=int(input('enter the number  '))
checkPrime=[True]*(N+1)
checkPrime[0]= checkPrime[1]=False

def isPrime(n):
    for k in range(n):
        if checkPrime[k] == True:
            return(True)
        
def markMultiplesFalse(j):
    for i in range(j, N+1, j):
        checkPrime[i]=False
            
def checkNo(n):
    for i in range(1,N):
        if isPrime(i):
            print(i)
            markMultiplesFalse(i)
checkNo(N) 


N=int(input('enter the number  '))
size=(N-3)//2 +1
isPrime=[True]*size
primes=[2]
        
def markMultiplesFalse(a):
    p=2*a +3
    for i in range(2*a**2 + 6*a + 3, size, p):
        isPrime[i]=False
            
for i in range (size):
    if isPrime[i]:
        primes.append(2*i+3)
        markMultiplesFalse(i)
print(primes)
