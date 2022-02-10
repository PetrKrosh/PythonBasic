guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    new_guest = input('Input new guest: ')
    commamd = input('Input COMMAND: Add, Remove: ')
    if commamd == 'Add':
        if len(guests) <= 5:
            guests.append(new_guest)
        else:
            print('There are no free place')
    if commamd == 'Remove':
        if new_guest in guests:
            guests.remove(new_guest)
        else:
            print('Such is mising ')
    if commamd == 'sleep':
        break
print(guests)
