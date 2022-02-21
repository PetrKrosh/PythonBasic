count_sticks = 10
count_shots = 2

list_stick = list(range(1, count_sticks+1))

for i in range(1, count_shots +1):
    A = int(input('Input left num: '))
    B = int(input('Input right num: '))
    list_stick = [i if not(A<=i<=B) else 0 for i in list_stick]
print(list_stick)

L_new = ['.' if i == 0 else 'I' for i in list_stick]
print(*L_new)