n = int(input("Enter a number: "))
if n < 0:
    print("Not defined for negative numbers.")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial:", result)
