import tkinter as tk
import requests
from tkinter import Tk, Label, Button 


window = tk.Tk()

window.title('Выводит json файл и сохраняет')
window.geometry('300x200')


def get_text():
    
    integ =int(entry.get()) 
    print(type(integ))
    url = f'https://jsonplaceholder.typicode.com/todos/{integ}'

    req = requests.get(url)
    with open(f'data{integ}.json','w') as file:
            file.write(req.text)
    g=req.text


label = Label(window, text='введите ID: ')
entry = tk.Entry(window)

button = tk.Button(window, text="сохранить", command=get_text)
label.pack()
entry.pack()
button.pack()
window.mainloop()