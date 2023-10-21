import random

numbers = {}

while True:
    CARD = input('Напишите номер вашей карточки на задней стороне чтобы пройти проверку НА БОТА: ')

    randoom = random.randint(1,2)

    if randoom == 1:
        print ('Вы успешно прошли проверку')
        break
    else:
        print(' А вдруг ты двоичное создание')

while True:
    comanda = input('Напиши команду /help : ')
    
    if comanda == '/help':
        
        print('Есть команда /YesOrNo, /add, /del, /see')
        
    if comanda == '/YesOrNo':
        while True:
            vopros = input('Напиши предсказание для бота, команда /exti означает выход: ')
            
            if vopros == '/exti':
                break
            
            otvet = random.randint(1, 2)
            
            if otvet == 1:
                print ('да')
            else:
                print ('нет')
                
    if comanda == '/see':
        print ('НА', numbers)
        
    if comanda == '/add':
        dobavu = input('Напиши имя: ')
        dobavu2 = input('Напишите номер телефона. Мы не будем вас отслеживать по айпи: ')
    
        numbers[dobavu] = dobavu2
        
    if comanda == '/del':
        ydalut = input('Напишите что вы хотите удалить: ')
        
        del numbers[ydalut]
        print ('Вы успешно удалили, Но в базах данных мы оставим)')
            
        