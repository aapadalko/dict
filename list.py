a = int(input('введите целое число, пределяющее длину списка: '))
b = int(input('введите целое число, определяющее максимальное значение списка: '))
x = [i for i in range(1, a + 1)]
y = [i for i in x if i <= b]
print(y)