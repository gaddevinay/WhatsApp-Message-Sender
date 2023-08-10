import pyautogui as pg
import tkinter as tk
from tkinter import messagebox
import time
window=tk.Tk()
window.title("Whatsapp Message Sender")
window.geometry('550x300')
label1=tk.Label(window,text="Enter the message want to send:",font=("Arial Bold",12))
label1.grid(row=0, column=0, padx=7, pady=7)
entry1=tk.Entry(window,width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2 = tk.Label(window, text="Enter the number of times to send:",font=("Bold",12))
label2.grid(row=1, column=0, padx=7, pady=7)
spinbox1 = tk.Spinbox(window, from_=1, to=25, width=5)
spinbox1.grid(row=1, column=1, padx=7, pady=7)
def clicked():
    label.configure(text="Place the Cursor on Whatsapp Message Box\nStarting in 10 seconds.....!\n ")
    messagebox.showinfo("Starting in 10 seconds...","Place the Cursor on Whatsapp Message Box")
    mess=entry1.get()
    times=spinbox1.get()
    window.update()
    time.sleep(10)
    for _ in range(int(times)):
        pg.write(mess)
        pg.press("Enter")        
label=tk.Label(window,font=("Arial Bold",17))
label.grid(row=2, column=0, columnspan=2, padx=7, pady=7)
button=tk.Button(window,text="START",command=clicked,width=15,height=1,font=("Serif Bold",12))
button.grid(row=3, column=0, columnspan=2, padx=7, pady=7)
window.mainloop()
