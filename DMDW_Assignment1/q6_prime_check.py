def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")


n = int(input("Enter the number: "))
prime(n)
