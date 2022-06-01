n = str(input("請輸入數字:"))
n1 = str((int(n[0])+7)%10)
n2 = str((int(n[1])+7)%10)
n3 = str((int(n[2])+7)%10)
n4 = str((int(n[3])+7)%10)
ans = n3+n4+n1+n2
print("輸出加密後的數字為:",ans)
