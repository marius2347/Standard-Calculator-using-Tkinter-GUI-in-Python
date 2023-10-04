import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

window.minsize(470, 700)
window.maxsize(470, 700)
window.configure(bg="#121212")

# Frame with background
first_row_frame = tk.Frame(window, bg="#2FDDB3")
first_row_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Label for credits
credits = tk.Label(
    first_row_frame,
    text="by Marius",
    anchor="e",
    justify="right",
    fg="white",
    bg="#2FDDB3"
)

# Label for standard text
lefText = tk.Label(
    first_row_frame,
    text="Standard",
    anchor="w",
    justify="left",
    font=("Arial", 25, 'bold'),
    fg="white",
    bg="#2FDDB3"
)

# Place each label in the same row
lefText.grid(row=0, column=0, padx=0, pady=10)
credits.grid(row=0, column=1, padx=0, pady=10)

# Function
def on_button_click(event):
    current_text = result_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + button_text)

# Store the result
result_var = tk.StringVar()
result_var.set("")

# Display the result
result_entry = tk.Entry(window, textvariable=result_var, font=("Helvetica", 30), bg="#121212", fg="white", )
result_entry.grid(row=1, column=0, padx=10, pady=40, columnspan=4)


# Buttons layout
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

# Third row
row_val = 2
col_val = 0

# Show the buttons in their position
for button_text in buttons:
    button = tk.Button(window, text=button_text, padx=40, pady=30, bg="#121212", fg="white", activebackground="purple", font=("Helvetica", 20))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


# Run the application
window.mainloop()
