n = int(input("請輸入正整數:"))
list = []

for i in range(1,n):
    if n%i == 0:
        list.append(i)



ans=0
for i in range(len(list)):
    ans += list[i]

if n==ans:
    print("perfect")
elif n>ans:
    print("deficient")
else:
    print("abundant")    