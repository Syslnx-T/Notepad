import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleText(tk.Text):
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')
        self.current_open_file = None
        
    
    # New file structure
    def new_file(self):
        self.text_area.delete(1.0, 'end')
        self.current_open_file = None


    # Open file structure
    def open_file(self):
        file_name = filedialog.askopenfilename()
        if file_name:
            self.text_area.delete(1.0, 'end')
            with open(file_name) as file:
                self.text_area.insert('end', file.read())
                self.current_open_file = file_name

    # Save file structure
    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()
            if new_file_path:
                with open(new_file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, 'end'))
                self.current_open_file = new_file_path
        else:
            with open(self.current_open_file, 'w') as file:
                file.write(self.text_area.get(1.0, 'end'))


    # Exit application
    def quit_confirm(self):
        if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            self.root.destroy()

root = tk.Tk()
root.geometry('800x600')

editor =SimpleText(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label='New', command=editor.new_file)
menu_options.add_command(label='Open', command=editor.open_file)
menu_options.add_command(label='Save', command=editor.save_file)
menu_options.add_command(label='Exit', command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label='File', menu=menu_options)

if __name__ == '__main__':
    root.title('Notepad')
    root.mainloop()