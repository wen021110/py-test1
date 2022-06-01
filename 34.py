n = int(input("輸入一個正整數:"))
if (n%2==0) and (n%11==0) and (n%5 != 0) and (n%7 != 0):
    print("22為新公倍數?yes")
else:
    print("22為新公倍數?no")