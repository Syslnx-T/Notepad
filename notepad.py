import tkinter as tk
from tkinter import filedialog, messagebox
root = tk.Tk()

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label='New')
menu_options.add_command(label='Open')
menu_options.add_command(label='Exit', command=root.quit)

root.config(menu=menu_bar)
menu_bar.add_cascade(label='File', menu=menu_options)







if __name__ == '__main__':
    root.title('Notepad')
    root.mainloop()