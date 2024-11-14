import tkinter as tk

root = tk.Tk()
root.title("MY APP")

label = tk.Label(root, text="hi its zylox")
label.pack()

def on_button_click():


 button = tk.Button(root, text="click here",
command= on_button_click)
 button.pack(pady=20)

label = tk.Label(root, text="click here please")
label.pack()

root.mainloop()


