import tkinter as tk

root = tk.Tk()
root.title(" Calculator")
root.geometry("320x420")
root.resizable(False, False)

expression = ""

display = tk.Entry(root, font=("Arial", 22), justify="right")
display.pack(fill="x", padx=10, pady=10, ipady=10)


def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    display.delete(len(display.get()) - 1, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "%", "+"),
    ("C", "DEL", "=")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for value in row:
        if value == "=":
            command = calculate
        elif value == "C":
            command = clear
        elif value == "DEL":
            command = delete
        else:
            command = lambda v=value: press(v)

        tk.Button(
            frame, text=value, font=("Arial", 16),
            command=command
        ).pack(side="left", expand=True, fill="both")

root.mainloop()
