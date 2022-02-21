str = input('Input str: ')
str_list = str.split()
longest = 0
longest_word = 0
for i in str_list:
    if len(i) > longest:
        longest = len(i)
        longest_word = i
print('Самое длинное слово: ', longest_word)
print('Длина это слова равна: ', longest)





















# text = input('Введите текст: ').split()
# length = 0
# line = ''
#
# for i_word in text:
#     if length < len(i_word):
#         length = len(i_word)
#         line = i_word
#
# print('Самое длинное слово в строке: "{0}", его длина {1}'.format(line, length))
