import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def analyze_color(image_path):
    with Image.open(image_path) as img:
        colors = img.getcolors(img.size[0] * img.size[1])
        average_color = tuple(sum([c[0] * c[1][i] for c in colors for i in range(3)]) // sum([c[0] for c in colors]) for j in range(3))
        return average_color

def show_image(image_path):
    with Image.open(image_path) as img:
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo

def get_file():
    file_path = filedialog.askopenfilename(title="Select Image File")
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)
        get_color()

def get_color():
    image_path = entry.get()
    color = analyze_color(image_path)
    color_hex = '#{:02x}{:02x}{:02x}'.format(*color)
    color_label.config(text=f"Average color: {color_hex}")
    show_image(image_path)

root = tk.Tk()
root.title("Color Analyzer")
root.geometry("400x400")

label1 = tk.Label(root, text="Select an image:")
label1.pack()

button = tk.Button(root, text="Open File", command=get_file)
button.pack()

entry = tk.Entry(root)
entry.pack()

analyze_button = tk.Button(root, text="Analyze color", command=get_color)
analyze_button.pack()

color_label = tk.Label(root, text="")
color_label.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
