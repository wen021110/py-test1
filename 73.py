time1 = input("輸入時間(時:分:秒):")
time2 = input("輸入時間:")

ans1 = time1.split(":")
timetotal1 = int(ans1[0])*60*60+int(ans1[1])*60+int(ans1[2])
print(timetotal1)

timetotal2 = int(time2)/(60*60)
timetotal3 = (int(time2)-(int(timetotal2)*3600))/60
timetotal4 = (int(time2)-(int(timetotal2)*3600)-(int(timetotal3)*60))
print(int(timetotal2),":",int(timetotal3),":",int(timetotal4))
