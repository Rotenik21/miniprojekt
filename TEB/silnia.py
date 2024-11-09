number = int(input("Wprowadź liczbę: "))
result = 1
while number > 1:
    result *= number
    number -= 1

print(result)