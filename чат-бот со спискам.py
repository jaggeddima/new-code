import time

spisok = []

vubor = ""

print ("Бот: Драсте вы нежданые гости но я бот со списками работать")
commands = 1

time.sleep (1)

print ("")
print ("------------------------------------------------------------------------ Команда номер:", commands)
print ("")

while True:
    print ("Список равняется", spisok)
    vubor = input("Бот: Напишите командку которую бот будет выполнять (Добавить в список, Я гавно, Удалить из списка, Просмотор элеиента и выйти): ")

    if vubor == "Выйти":
        time.sleep (0.5)
        
        print ("Бот: Итак программа выключается")
        break
    
    elif vubor == "Я гавно":
        time.sleep (0.25)
        
        print ("Бот: Подверждаю")
        
    elif vubor == "Добавить в список":
        time.sleep (0.25)
        
        spisok.append(input("Бот: Добавте что-то в список (в самом конце будет): "))
        
    elif vubor == "Удалить из списка":
        time.sleep (0.25)
        
        spisok.remove(input("Бот: Удалите то что находится в списке (название слово в списке): "))
        
    elif vubor == "Просмотр списка":
        time.sleep (1)
        
        nado = int(input("Напишите индекс списка: "))
        print (spisok[nado])
        
    else:
        time.sleep (0.25)
        
        print ("Программа не может определить  (error 404)")
        
    commands += 1
        
    time.sleep (1)
    print ("")
    print ("------------------------------------------------------------------------ Команда номер:", commands)
    print ("")








#   g
#   g
#   g
#   g
#gggggggg
