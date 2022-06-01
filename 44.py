from pickle import TRUE


c = int(input("輸入班級數:"))
list =[]
for i in range(c):
    if c>=1 and c<10:
        n = str(input("輸入班級人數:"))
        list.append(n)
    else :
        break
    list.sort(reverse=False)
print(list[0])