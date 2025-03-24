from PIL import Image
import os
from rembg import remove
from customtkinter import filedialog
import customtkinter as custom
window = custom.CTk()
height = window.winfo_screenmmheight()
width = window.winfo_screenmmwidth()
window.title("Background Eraser!")
window.geometry("{}x{}".format(height,width))
window.iconbitmap("icon.ico")
def file():
    filepath = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    directory = os.path.expanduser(f"~\Downloads\\")
    outpath = f"{directory}out.png"
    image_open = Image.open(filepath)
    image_removed = remove(image_open)
    image_removed.save(outpath)
    print(f"Imagem salva como {outpath}")
button = custom.CTkButton(window, command=file, width=100, height=100)
button.place(x=0, y=0)
window.mainloop()