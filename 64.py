n1 = int(input("請輸入第一個要判斷的數字:"))
n2 = int(input("請輸入第二個要判斷的數字:"))

if (n1%2==1) and ((n1+2)%2==1):
    if (n2%2==1) and ((n2+2)%2==1):
        print("y")
    else:
        print("n")
else:
    print("n")