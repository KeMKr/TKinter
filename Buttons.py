#First Tkinter Notepad

import tkinter as tk
import os

class ToDoData:

    def __init__(self):
        data_file = open("C:/Users/Kevin/Documents/Tkinter/To_do_list.txt", "a")
        data = eval(data_file)

    def add_task(str):
        pass

    def read_file(self):
        data_read = []
        for task in data.keys():
            data_read.append(task)
        return data_read

class Display:

    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()
        
        self.button = tk.Button(frame, text="Close", command=frame.quit)
        self.button.pack()

        self.hello = tk.Button(frame, text="Hello", command=self.say_hello)
        self.hello.pack()

        self.show_list = tk.Button(frame, text="Show List", command=self.show_list)
        self.show_list.pack()

        self.add = tk.Button(frame, text="Add to list", command=self.add_to)
        self.add.pack()

    def say_hello(self):
        print("Howdy")

    def add_to(self):
        add_screen = tk.Toplevel(width=100, height=100)
        add_screen.pack()

    def show_list(self):
        show = tk.Label(text = ToDoData.read_file(), width=100, height=10)
        show.pack()

root = tk.Tk()
window = Display(root)

root.mainloop()
root.destroy()

