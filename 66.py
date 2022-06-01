a = str(input("請輸入string_a:"))
b = str(input("請輸入string_b:"))

sa = set(a)
sb = set(b)

ans = list(sa & sb)
ans.sort()
if (len(ans)==0):
    print('n')
else:
    for i in range(len(ans)):
        print(ans[i],end = '')