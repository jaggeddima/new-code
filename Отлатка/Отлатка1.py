import time

while True:
    Command = input('Command: Pleas check what u need. "Load_txt" or "Correct_txt": ')
    
    if Command == 'Load_txt':
        
        txt = open('Отлатка1.txt','r')
        
        print(txt.readline())
        txt.close()
        
    if Command == 'Correct_txt':
        
        txt = open('Отлатка1.txt','w')
        
        txt.write(input())
        txt.close()