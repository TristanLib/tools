from tkinter import Tk, filedialog, Button, Label
from PIL import Image
import os

# Function to convert jpg to png
def convert_jpg_to_png(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg'):
                img = Image.open(os.path.join(folder_path, filename))
                new_filename = os.path.splitext(filename)[0] + '.png'
                img.save(os.path.join(folder_path, new_filename))
        return "Conversion Successful"
    except Exception as e:
        return f"An error occurred: {e}"

# Function to open folder dialog and set folder path
def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        status = convert_jpg_to_png(folder_path)
        status_label.config(text=status)

# GUI setup
root = Tk()
root.title("JPG to PNG Converter")
root.geometry("400x600")
open_folder_btn = Button(root, text="Choose Directory", command=open_folder_dialog)
open_folder_btn.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
