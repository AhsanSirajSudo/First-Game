import tkinter as tk

root = tk.Tk()
root.title("Game Window")
root.geometry("900x600")
root.configure(background="yellow")

text = tk.Label(root, text = ("Hey monkey"),font = ("Poppins",24))
text.place(x=64,y=128)
root.mainloop()

