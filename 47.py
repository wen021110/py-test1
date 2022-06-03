n = int(input("輸入筆數:"))
if (n>4):
    print("超出範圍")
elif (n==4):
    n1 = input("金:")
    n2 = input("銀:")
    n3 = input("銅:")
    n4 = input("優:")
    print("金牌得到",n1,"面")
    print("銀牌得到",n2,"面")
    print("銅牌得到",n3,"面")
    print("優牌得到",n4,"面")
elif (n==3):
    n1 = input("金:")
    n2 = input("銀:")
    n3 = input("銅:")
    print("金牌得到",n1,"面")
    print("銀牌得到",n2,"面")
    print("銅牌得到",n3,"面")
elif (n==2):
    n1 = input("金:")
    n2 = input("銀:")
    print("金牌得到",n1,"面")
    print("銀牌得到",n2,"面")
elif(n==1):
    n1 = input("金:")
    print("金牌得到",n1,"面")
else:
    print("輸入錯誤")