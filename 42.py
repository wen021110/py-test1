a = int(input("輸入a值:"))
b = int(input("輸入b值:"))
c = int(input("輸入c值:"))
x3=4**0.5

if (b**2-4*a*c) > 0:
    x1 = (-b+ (b**2-4*a*c)**0.5)/2*a
    x2 = (-b- (b**2-4*a*c)**0.5)/2*a
    print(x1)
    print(x2)
elif (b**2-4*a*c) == 0:
    x1 = (-b)/2*a
    print(x1)
elif (b**2-4*a*c) < 0:
    print("0")
    