# Calculate Factorial of a Number

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")

else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "is", factorial)
