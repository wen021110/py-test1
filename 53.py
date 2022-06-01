k = float(input("請輸入公里數:"))

k1 = round((k*1000-1500)/250)

if k1 <= 0:
    total = 75 
    print(total)
else:
    total = 75 + 5*k1
    print(total)