import tkinter as tk

root = tk.Tk()

def key(event):
    print(repr(event.char), repr(event.keysym), repr(event.keycode))

root.bind("<Key>", key)
root.mainloop()