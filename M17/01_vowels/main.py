text = input('Введите текст: ')
vowels_list=['у','е', 'а','о','я', 'и', 'ю']

vowels_in_text = [i for i in text if i in vowels_list]
print(vowels_in_text)
print(len(vowels_in_text))