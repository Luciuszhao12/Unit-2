def gcf(number1, number2):
    a = abs(number1)
    b = abs(number2)

    while b !=0:
        a, b = b, a % b
    return a 

number1 = int(input("Whats the first number?"))
number2 = int(input("Whats the second number?"))


print(gcf(number1, number2))