ans = str(input("輸入四位數字"))
qu = str(input("輸入四位數字:"))
a = 0
b =0
while (qu != ans):
    for i in qu:
        for j in ans:
            if i == j:
                if qu.index(i) == ans.index(j):
                    a += 1
                else:
                    b += 1
    print(a,"A",b,"B")
    a = 0
    b = 0
    qu = str(input("輸入四位數字:"))