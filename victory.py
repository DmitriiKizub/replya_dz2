bill = '1955'
djon = '1839'
kar = '1835'
ford = '1863'
game= None
while game != 'Нет':
    print('Введите даты рождений:')
    bill_in= input('Билл: ')
    djon_in = input('Джон: ')
    kar_in = input('Карнеги: ')
    ford_in = input('Форд: ')
    a=0
    if bill == bill_in:
        a+=1
    if djon == djon_in:
        a+=1
    if kar  == kar_in:
        a+=1
    if ford  == ford_in:
        a+=1

    print("Верных ответов: ", a)
    print("Кол-во ошибок: ", 4-a)
    print("Процент ", a/4*100, '%')
    game = input('Продолжить играть? ')

print('end')