n = int(input("輸入一個金額:"))
n1 = int(n/100)
n2 = int((n-n1*100)/50)
n3 = int((n-n1*100-n2*50)/10)
n4 = int((n-n1*100-n2*50-n3*10)/5)
n5 = int((n-n1*100-n2*50-n3*10-n4*5))

total = n1+n2+n3+n4+n5
print(total)
