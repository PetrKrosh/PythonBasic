#--Вариант 2--------------------------------
while True:
    password = input('Придумайте пароль: ')
    if len(password) > 8 and not password.islower() and not password.isalpha():
        num = [i for i in password if i.isdigit()]
        if len(num) >= 3:
            print('Пароль надёжный')
            break
    else:
        print('Пароль не надежный!')

#--Вариант 1--------------------------------
# sym_is_upper = 0
# sym_is_number = 0
#
# while True:
#     password = input('Придумайте пароль: ')
#
#     if len(password) >= 8:
#         for sym in password:
#             sym_is_number += sym.isdigit()
#             sym_is_upper += sym.isupper()
#         if sym_is_number < 3:
#             print('Пароль ненадёжный. Число цифр должно быть не менее 3 шт')
#         elif sym_is_upper < 1:
#             print('Пароль ненадёжный. Число звглавных букв должно быть не менее 1 шт')
#         else:
#             print('Это надёжный пароль!')
#             break
#
#     else:
#         print('Пароль ненадёжный.Длина должна быть не менее 8 символов!')
