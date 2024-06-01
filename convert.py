import tkinter as tk

def decimal_to_binary():
    try:
        decimal_num = int(input_field.get())
        binary_num = bin(decimal_num).replace("0b", "")
        output_label.config(text=f"Binary: {binary_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a decimal number.")

def binary_to_decimal():
    try:
        binary_num = input_field.get()
        decimal_num = int(binary_num, 2)
        output_label.config(text=f"Decimal: {decimal_num}")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid binary number.")

def clear_output():
    output_label.config(text="")

root = tk.Tk()
root.title("Binary-Decimal Converter")
root.geometry("650x650")

input_field = tk.Entry(root)
input_field.place(x=150, y=50, width=300)

decimal_to_binary_button = tk.Button(root, text="Decimal to Binary", command=decimal_to_binary)
decimal_to_binary_button.place(x=150, y=80, width=140)

binary_to_decimal_button = tk.Button(root, text="Binary to Decimal", command=binary_to_decimal)
binary_to_decimal_button.place(x=300, y=80, width=140)


output_label = tk.Label(root, text="", pady=10)
output_label.place(x=200, y=150)


clear_button = tk.Button(root, text="Clear", command=clear_output)
clear_button.place(x=275, y=110)

root.mainloop()