n = int(input("輸入整數N:"))
for i in range(n+1):
    for j in range(0,n-i):
        print("",end=" ")
    for j in range(n-i,n):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1,n):
        print("",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    
    print()
