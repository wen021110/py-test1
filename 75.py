from pickle import TRUE


list = []

while True:
    n = str(input("請輸入事項(若以無事項，請輸入end):"))
    if n=="end":
        break
    else:
        list.append(n)

for i in range(len(list)):
    print("第",i+1,"項",list[i])