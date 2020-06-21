a = int(input('введите число А: '))
b = int(input('введите число Б: '))
c = int(input('введите число В: '))
while a <= b:
        print(a, "- Пока что нет")
        a = a + c
print('Дождались! -', a)