import time

class NPC:
    
    def __init__(self, n, h, xp, p, s):
        
        self.name = n
        self.height = h
        self.xp = xp
        self.pr = p
        self.spisoktovarov = s
        
    def Pr(self):
        if self.pr == 'Сапожник':
            print('Дарова холоп, ВИДИШЬ ЧТО ЗА ТОВАРЫ МОЖЕШЬ КУПИТЬ (',self.spisoktovarov, #NPC1 - Сапожник
              ') И Я ТЕБЕ НЕ БУДУ ГОВОРИТЬ ХТО Я ПОТОМУЧТО ТЫ ХОЛОП ######')
        elif self.pr == 'Шахтёр':
            print('Привит чиловик. Миня зовут',self.name,'И вот маи тавары,',self.spisoktovarov #NPC2 - Шахтёр
                  ,'Пакупая все што ты хочиш')
        else:
            print('Здрасте, вот мои товары, ',self.spisoktovarov)
            
    def Poka(self):
        if self.pr == 'Сапожник':
            print('ПОШЁЛ ТЫ #####')
        elif self.pr == 'Шахтёр':
            print('Пака игрок')
        else:
            print('До свидание игрок')

NPC_1 = NPC('Генадий', '126', '94', 'Сапожник', 'Ботинок николай')
NPC_2 = NPC('Димон', '211', '1', 'Шахтёр', 'Алмаз, Факел, Железо, Уголь, Раба')
NPC_3 = NPC('Мистер Зайкин', '187', '54', 'Учёный', 'Шёколадку, Огурец, Бана')

NPC_1.Pr()
time.sleep(10)
NPC_1.Poka()
time.sleep(1)
NPC_2.Pr()
time.sleep(10)
NPC_2.Poka()
time.sleep(1)
NPC_3.Pr()
time.sleep(10)
NPC_3.Poka()
        