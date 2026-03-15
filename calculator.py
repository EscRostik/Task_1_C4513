a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
x = input("Введіть дію (+ - * /): ")

if x == "+":
    print("Результат:", a + b)
elif x == "-":
    print("Результат:", a - b)
elif x == "*":
    print("Результат:", a * b)
elif x == "/":
    if b == 0:
        print("Ділення на нуль!")
    else:
        print("Результат:", a / b)