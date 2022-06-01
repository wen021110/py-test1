i = input(str("輸入為兩列字串(str1,str2):")) 

str1 = i.split(",")

if str1[0] in str1[1]:
    print("YES")
else:
    print("NO")