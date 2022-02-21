def search_symbol(str, symbol):
    list_finish = []
    for i in range(len(str)):
        if str[i] == symbol:
            list_finish.append(i)
    return list_finish

str= 'ashdfhvhdf'
listt= search_symbol(str, 'h')

print('Развёрнутая последовательность между первым и последним h:', str[listt[0]+1:listt[-1]])