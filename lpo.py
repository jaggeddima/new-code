import time
import random

print ("Вы шли по тропинки и у вас выбор: ")
mojang = input("Либо идите на право либо на лево: ")
i=0

# First Chapter

while True:
    while mojang != "на лево" and mojang != "на право":
        mojang = input("Либо идите на право либо на лево: ")
    if mojang == "на право":
        time.sleep (2)
        mojang = input("Game over, Либо идите на право либо на лево: ")
    elif mojang == "на лево":
        break
    
time.sleep (1)

# Second Chapter

print ("Спустя пол часа ты нашёл крепость и тропинку")
time.sleep (0.25)
lol = input("Войти или идти дальше: ")

while True:
    while lol != "войти" and lol != "идти дальше":
        lol = input("Войти или идти дальше: ")
    if lol == "войти":
        i = 5
        break
    elif lol == "идти дальше":
         lol = input("Войти или идти дальше: ")
         
# Third Chapter
           
print ("Вас взяли и превели к корол делать допрос")
print("отвечайте да или нет")
# First Pre-Chapter
while True:
    l1 = input("Король: Ты прибыл для того чтобы я дал тебе денег? : " )
    if l1 == "нет":
        break
    if l1 == "да":
        i = 5
# second Pre-Chapter
while True:
    l2 = input("Король: Ты просто так проишёл? : " )
    if l2 == "да":
         break
    if l2 == "нет":
        i = 5
# third Pre-Chapter
while True:
    l3 = input("Король: Ты чтоли шпион? : " )
    if l3 == "нет":
        break
        l = 6
    if l3 == "да":
        i = 5

# Fourth Chapter

time.sleep (2)

lpl = input("Дальше или выйти из программы? : ")

while True:
    if lpl == "дальше":
        lpl = input("Простите игра закончена. Дальше или выйти из программы? : ")
    elif lpl == "выйти":
        break

print ("Прощаюсь :)")
        

    
        
        
            
    
        
