shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

tovar = input('Input TOVAR for soach: ')
cont_tovar = 0
summ = 0
for i in shop:
    if i[0] == tovar:
        cont_tovar += 1
        summ += i[1]
print(cont_tovar)
print('Товара ', tovar, 'на сумму ', summ)











# detail = input('Введите название детали: ')
# detail_count = 0
# num_detail = 0
#
# for i_detail in shop:
#     if i_detail[0] == detail:
#         detail_count += 1
#         num_detail += i_detail[1]
#
# print('Кол-во деталей -', detail_count)
# print('Общая стоимость -', num_detail)
