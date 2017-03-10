from Tkinter import *

root = Tk()

canvas = Canvas(root, bg='black', width = 512, height = 512)
canvas.pack()

a1 = canvas.create_oval(100, 100, 500, 500, fill='red')

root.mainloop()
