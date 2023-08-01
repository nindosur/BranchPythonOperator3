# 1
value1 = input('Введите шестизначное число: ')
if len(value1) != 6:
    print('Число не шестизначное')
else:
    lst = list(map(int, list(value1)))
    first, last = lst[:3], lst[3:]

    if sum(first) == sum(last):
        print('Счастливое')
    elif sum(first) != sum(last):
        print('Число не счастливое')

# 2
number = input('Введите шестизначное число: ')
if not len(number) == 6:
    print('Введите шестизначное число!')
else:
    print(number[-1]+number[-2]+number[2:-2]+number[1]+number[0])

# 3
value2 = int(input("Введите номер месяца: "))
if value2 in [1,2,12]:
    print(value2, "- Winter!")
elif value2 in [3,4,5]:
    print(value2, "- Spring!")
elif value2 in [6,7,8]:
    print(value2, "- Summer!")
elif value2 in [9,10,11]:
    print(value2, "- Autumn")
else:
    print("В году всего 12 месяцев!")

