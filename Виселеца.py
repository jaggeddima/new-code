import time

NADO = input("Введите слово (6 букв надо) через пробел: ")
clovo = NADO.split( )
clovo2 = []

popytka = 10
ocko = 0

for i in 1, 2, 3, 4, 5, 6:
      print ("")
while True:
    print ("-----------------------------------------------------------------------")
    print ("Очки:", ocko, "Попытки", popytka, "Буквы которые ты угадал:",clovo2)
    Bykva = input("Напишите букву которая вам кажется что она есть (Слово на англиском): ")
    
    if Bykva in clovo:
        time.sleep (1)
        
        print ("Эта буква в слове есть!")
        ocko += 1
        
        clovo.remove (Bykva)
        clovo2.append (Bykva)
        
    else:
        time.sleep (1)
        
        print ("Этой буквы НЕТУ")
        popytka -= 1
        
    if popytka == 0:
        break
        print ("You are KILLING")
        
    if ocko == 6:
        break
        print ("You are WIN")
    