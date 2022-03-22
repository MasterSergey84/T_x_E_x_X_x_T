text = input('Введите текст: ')
dlina = int(len(text))
x = 0
if dlina > 1:
    print('Получившийся текст: ', end='')
    while x < dlina:
        if (x + 1) == dlina:
            print(text[x], end='')
            break
        if text[x + 1] != ' ':
            print(text[x], '*', sep='', end='')
            x += 1
        else:
            print(text[x], text[x+1], sep='', end='')
            x += 2
    print()
else:
    print('Получившийся текст:', text)
