import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Digital Calculator")

# Create the entry widget to display the input and output
entry = tk.Entry(root, font=("Helvetica", 20), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create the button grid for digits and operations
buttons = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("C", "0", "=", "/")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for text in row:
        btn = tk.Button(frame, text=text, font=("Helvetica", 20), relief="ridge", borderwidth=3)
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()
