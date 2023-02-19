spisok = [[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]
while True:
    x=int(input("Кординаты x: "))
    y=int(input("Кординаты y: "))
    if x > 5 or y > 5:
        print ("НЕ ПОНЯТНО")
    spisok [y][x] = "q"
    
    for i in spisok :
        for g in i:
            print (g, end = " ")
        print ()
    #print ("Кординаты:", spisok)
    
    
    
