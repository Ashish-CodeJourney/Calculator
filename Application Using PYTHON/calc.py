import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def add_to_input(value):
    entry.insert(tk.END, value)

def create_button(root, text, row, column, bg="#4a4a4a", fg="#ffffff", width=1, height=1, command=None):
    button = tk.Button(root, text=text, bg=bg, fg=fg, width=width, height=height, font=("Arial", 24),
                       command=lambda: add_to_input(text) if command is None else command())
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    return button

root = tk.Tk()
root.title("Calculator - By Ashish-CodeJourney")
root.configure(bg="#0a0a0a")  

frame = tk.Frame(root, bg="#0a0a0a")
frame.pack(expand=True, fill="both")

entry = tk.Entry(frame, font=("Arial", 32), bg="#0a0a0a", fg="#ffffff", bd=0, insertbackground="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('00', 4, 1), ('.', 4, 2), ('+', 4, 3),
]

for button_info in buttons:
    create_button(frame, *button_info)

create_button(frame, "AC", 5, 0, bg="#6dee0a", command=clear)
create_button(frame, "DEL", 5, 1, bg="#6dee0a", command=lambda: entry.delete(len(entry.get()) - 1, tk.END))
create_button(frame, "%", 5, 2, bg="#6dee0a", command=lambda: add_to_input("%"))
create_button(frame, "=", 5, 3, bg="#fb7c14", fg="#ffffff", height=2, command=calculate)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_rowconfigure(5, weight=1)

root.mainloop()
