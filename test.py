import pyautogui
import time

l = True

while l == True:
    vubor = input("Enter: Random, autoclicker, Game")
    time.sleep(2)
    if vubor == "1":

        pyautogui.write("import random", interval=0.05)
        time.sleep (0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.write("n1 = random.randint(1, 10)", interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("while True:", interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("print (n1)", interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.write("n1 = random.randint(1, 10)", interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')

    elif vubor == "2":

        pyautogui.write("import pyatogui", interval=0.05)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.write("import time", interval=0.05)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.write("time.sleep (1)", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("while True:", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("pyautogui.click()", interval=0.05)
        pyautogui.press('enter')

    elif vubor == "3":

        pyautogui.write("import random", interval=0.05)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.write("n1 = int(input())", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("number = random.randint(1,10)", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("if n1 == number:", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("print(n1)", interval=0.05)
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.write("else:", interval=0.05)
        pyautogui.press('enter')
        pyautogui.write("print(n1)", interval=0.05)
        pyautogui.press('enter')

    elif vubor == "4":
        pyautogui.write ("Code in github.com", interval=0.05)
    elif vubor == "Exti":
        l = False
    else:
        print ("Ошибка ")
        time.sleep (0.2)
        print("Ошибка . ")
        time.sleep (0.2)
        print("Ошибка . . ")
        time.sleep (0.2)
        print("Ошибка . . .")

