def f(str):
    l = []
    c = str[0]
    print('c = ', c)
    for x in str:
        if x in c:
            c += x
            continue
        l.append(c)
        c = x
    l.append(c)
    return l

print(f('55544355'))
