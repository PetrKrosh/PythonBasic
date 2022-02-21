name_file = input('Input name file: ')

spetc_symbol = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
extention = ('.txt', '.docx')

if name_file.endswith(extention) == False:
    print('Uncorrect extention!')
elif name_file.startswith(spetc_symbol):
    print('Uncorrect start!')
else:
    print('OK!')