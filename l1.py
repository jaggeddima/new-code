print("кибербанка")
print()
print("вы попадаете в банку с вайфаем 5G и её волны плавит ваш мозг")
hod = input("выберите: разбить банку, выползти из неё, сделать из вайфая космический корабль и стать ситхом:")
while hod != "разбить банку" and hod != "выползти из неё" and hod != "сделать из вайфая космический корабль и стать ситхом":
    hod = input("выберите: разбить банку, выползти из неё, сделать из вайфая космический корабль и стать ситхом:")
if hod == "разбить банку":
    print("вы разбиваете банку. Последне, что вы видели - это большой осколок упавший на вас")
    print("Game over! станьте айм олвейс камбек")
    hod = input("скажите, что вы олвейс камбек: ")
    if hod == "стать айм олвейс камбек":
        print("вы разваливаете осколки банки, но из - за того, что вы олвейс камбек вайфай убил вас своими волнами")
        print("тотальный game over!")
        print("да/нет")
        hod=input("точно сломался?: ")
        if hod=="нет":
            print("в тебя вставили кучу кибер имплантов и ты пошёл ломать обезьянкам черепа")
            print("Победа")
        else:
            print("ты уже смерился со смертью и не один имплант тебя уже не спасёт...")
            print("хорошо/отстань")
            hod=input("быстро взял себя в руки: ") 
            if hod=="хорошо":
                print("В тебя воткнули блютуз и вайфай и теперь ты ноутбук на котором написана это истоия")
            else:
                print("на тебе сделали кучу операций. Ты обезумел и стал кибермакакой")
                print("Победа?")
            
elif hod == "выползти из неё":
     print("вы хотели выползти из кибербанки, но из - за того, что вы стали выше к вышке, корпорация кока-колы сожгла ваши мозги")
     print("game over!")
elif hod == "сделать из вайфая космический корабль и стать ситхом":
     print("через пот и слёзы от волн вышки вы ломаете её, делаете корабль и улетаете из банки")
     print("но из пустоты вылетают кибербанкиры и просят с вас киберналог")
     print("вырианты действий: заплатить им своим кораблём, улететь от них, сжечь их лазерами корабля")
     hod = input("введите: ")
     
     if hod == "заплатить им своим кораблём":
        print("вы отдаёте им свой корабль, и вас съедают сверх - быстрые киберобезьяны")
        print("Game over!")
        
     elif hod == "улететь от них":
        print("вы начинаете погоню, но вы с паники нечайно врезались в вышку и разбились")
        print("Game over!")
     elif hod == "сжечь их лазерами корабля":
        print("вы сжигаете их своми лучами 5G")
        print("Оказалось, что они были мега - корпорантами, которых ненавидел весь киберсити")
        print("Вы стали королём пустошей киберсити! Вы победили!")
