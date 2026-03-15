import random

x = random.randint(1, 10)

for i in range(3):
    guess = int(input("Вгадай число від 1 до 10: "))

    if guess == x:
        print("Правильно!")
        break
    elif guess > x:
        print("Менше")
    else:
        print("Більше")

if guess != x:
    print("Ти програв. Було число:", x)