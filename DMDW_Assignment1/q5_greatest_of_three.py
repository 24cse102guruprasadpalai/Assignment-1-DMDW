def greater(a, b, c):
    if a > b and a > c:
        print(a, "is the greatest")
    elif b > a and b > c:
        print(b, "is the greatest")
    elif c > a and c > b:
        print(c, "is the greatest")
    else:
        print("More than one number is same")


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
greater(a, b, c)
