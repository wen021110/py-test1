n = float(input("請輸入路程公里數:(km):"))
money = 75
if (n>1.5):
    if (n-1.5)<0.25:
        money += 5
    else:
        if ((n-1.5)%0.25==0):
            money += ((n-1.5)/0.25*5)
        else:
            money = money+((n-1.5)//0.25*5)+5
print("所需車資為:",round(money))
