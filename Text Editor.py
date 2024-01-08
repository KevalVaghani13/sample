import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def text_editor():
    def open_file():
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )

        if not filepath:
            return

        txt_edit.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f'Text Editor - {filepath}')

    def save_file():
        filepath = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
        )

        if not filepath:
            return

        with open(filepath, 'w') as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f'Text Editor - {filepath}')

    def exit_app():
        window.destroy()

    def cut_text():
        txt_edit.event_generate("<<Cut>>")

    def copy_text():
        txt_edit.event_generate("<<Copy>>")

    def paste_text():
        txt_edit.event_generate("<<Paste>>")

    def zoom_in():
        current_font_size = txt_edit.cget("font").split(" ")[-1]
        new_size = int(current_font_size) + 2
        txt_edit.config(font=(current_font_family, new_size))

    def zoom_out():
        current_font_size = txt_edit.cget("font").split(" ")[-1]
        new_size = max(2, int(current_font_size) - 2)
        txt_edit.config(font=(current_font_family, new_size))

    window = tk.Tk()
    window.title('Text Editor')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)


    menubar = tk.Menu(window)
    window.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save As...", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)

    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut_text)
    edit_menu.add_command(label="Copy", command=copy_text)
    edit_menu.add_command(label="Paste", command=paste_text)
    edit_menu.add_separator()
    edit_menu.add_command(label="Zoom In", command=zoom_in)
    edit_menu.add_command(label="Zoom Out", command=zoom_out)

    txt_edit = tk.Text(window, wrap="word")
    txt_edit.grid(row=0, column=1, sticky='nsew')

    # Default font settings
    current_font_size = 12
    current_font_family = "Arial"
    txt_edit.config(font=(current_font_family, current_font_size))

    window.mainloop()

if __name__ == '__main__':
    text_editor()
