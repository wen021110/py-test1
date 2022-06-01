password = str(input("檢測的字串(end結束):"))
checkword = str(input("檢測的單一字元:"))
n = 0
if password == "end":
    print("檢測結束")
else:
    n = password.count(checkword)
    print(n)