import pyautogui
import time

number1 = int(input("lol"))
number2 = int(input("lol"))

c = 0

lol = input()

if lol == "+":
    c = number1 + number2
if lol == "*":
    c = number1 * number2
if lol == "/":
    c = number1 / number2
if lol == "-":
    c = number1 - number2
    
time.sleep(1)
    
pyautogui.write(str(c), interval=0.05)