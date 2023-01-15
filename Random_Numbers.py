import random

i = 5
operation = 1
a = 1000

pos1 = random.randint (1, a)
pos2 = random.randint (1, a)

while i < 6 :
    print (pos1,pos2)

    if (pos1 == pos2):
        print ("Ура, Вот стока было сделано",
               "операцые для нахождение равных чисел:",
               operation)
        i = 6
    else:
        pos1 = random.randint(1, a)
        pos2 = random.randint(1, a)

        operation = operation + 1