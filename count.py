N = int (input("enter a number  "))
counter =0
for i in range (1,N+1):
    counter += str(i).count('0') 
print(counter)


