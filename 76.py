pw = str(input("輸入密碼:"))
if len(pw)==6:
    n1 = str(int(pw[0])*4%7)
    n2 = str(int(pw[1])*4%7)
    n3 = str(int(pw[2])*4%7)
    n4 = str(int(pw[3])*4%7)
    n5 = str(int(pw[4])*4%7)
    n6 = str(int(pw[5])*4%7)
    print("解密後的密碼:",n1+n2+n3+n4+n5+n6)
else:
    print("長度不足六個字元，請重新輸入")