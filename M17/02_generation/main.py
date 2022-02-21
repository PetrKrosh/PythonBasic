num = int(input('Введите длинну списка: '))

list = [1 if i%2 == 0 else i%5 for i in range(num)]

print(list)