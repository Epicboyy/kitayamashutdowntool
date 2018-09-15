from tkinter import *
from tkinter import ttk
import os

str1 = Tk()
str1.title("Ktayama Shutdown Tool")
str1.iconbitmap('C:/Users/ASUS/Downloads/1.ico')
str1.geometry('800x200')
Label(str1, text="此工具由北山所製作", font=(12)).pack()
button1 = ttk.Button(str1,text="關機")
button1.pack()
button2 = ttk.Button(str1,text="重新開機")
button2.pack()
button3 = ttk.Button(str1,text="登出使用者")
button3.pack()
button4 = ttk.Button(str1,text="休眠電腦")
button4.pack()
Label(str1, text="本城市依照GNU GPL公共授權條款 開源程式碼 : https://github.com/rootmelo92118/kitayamashutdowntool \n 更多詳情請上 : https://www.gnu.org", font=(5)).pack()

def shutdown():
    os.system("shutdown /s /t 0")
    
def reboot():
    os.system("shutdown /r /t 0")
    
def logout():
    os.system("shutdown /l")
    
def nibernate():
    os.system("shutdown /h")
    
button1.config(command=shutdown)
button2.config(command=reboot)
button3.config(command=logout)
button4.config(command=nibernate)
str1.mainloop()
