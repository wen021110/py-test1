t = int(input("搭了幾次電梯:"))
floor = 1
money = 0
for i in range(t):
    floor1 = int(input(":"))
    if floor1 > floor:
        money += (floor1-floor)*20
    elif floor1 < floor:
        money += (floor-floor1)*10
    floor = floor1
print(money)