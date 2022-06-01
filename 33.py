list = []
score1 = int(input("國文:"))
score2 = int(input("英文:"))
score3 = int(input("微積分:"))
score4 = int(input("體育:"))
score5 = int(input("程式設計:"))
list.append(score1)
list.append(score2)
list.append(score3)
list.append(score4)
list.append(score5)
total = len(list)
dict = {"國文":list[0],"英文":list[1],"微積分":list[2],"體育":list[3],"程式設計":list[4]}

avg = sum(list)/total
max = max(list)
min = min(list)

print("平均分數:",avg)
print("最高分科目:",max,"分")
print("最低分科目",min,"分")