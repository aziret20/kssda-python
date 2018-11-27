sm = 1
sc = 0
direct = 'right'
while True:
    if direct == 'right':
        SR()
        sc += 1
    else:
        SL()
        sc -= 1
    if check():
        if sc != 0:
            break
    if sc == sm:
        if direct == 'right':
            direct = 'left'
        else:
            direct = 'right'
    if sc == 0:
        sm += 1
        direct == 'right'
