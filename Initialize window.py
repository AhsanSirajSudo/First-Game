import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Game Window")
root.geometry("900x600")
root.configure(background="yellow")

imagefile = r"C:\Users\Ahsan\Downloads\billi.jpg"
opened_image = Image.open(imagefile)
img = ImageTk.PhotoImage(opened_image)

label = tk.Label(root, image=img)
label.pack()
label.image = img

text = tk.Label(root, text = ("Hey monkey"),font = ("Poppins",24))
text.place(x=64,y=128)
root.mainloop()

