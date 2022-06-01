a = input("請輸入a的好友:")
b = input("請輸入b的好友:")

af = set(a.split(" "))
bf = set(b.split(" "))

t = len(af & bf)
print(t)