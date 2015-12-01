ran = int(input('Search edge?'))
div = int(input('i % X = Y.\nx='))
remain = int(input('y='))
#
if(div>remain):
    Num = [i for i in range(1,ran)if i%div==remain]
    count = 1
    for x in Num:
        print(x,'',end='')
        if (not count%5): print('\n')
        count = count + 1
else: print('Input erro: Y cannot be bigger than X')

input('\nPress ENTER to finish.')
