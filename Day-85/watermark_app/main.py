import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

file_path = ""

window = tk.Tk()
window.title("Watermark App")
window.geometry("600x500")


def upload_image():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select an Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 300))

        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo


def add_watermark():
    watermark_text = watermark_entry.get()

    if not file_path or not watermark_text.strip():
        print("Please select an image and enter watermark text.")
        return

    image = Image.open(file_path).convert("RGBA")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Arial.ttf", 50)

    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = max(10, image.width - text_width - 20)
    y = max(10, image.height - text_height - 20)

    draw.text((x, y), watermark_text, fill=(255, 255, 255, 255), font=font)

    image.show()


upload_button = tk.Button(window, text="Choose Image", command=upload_image)
upload_button.pack(pady=20)

image_label = tk.Label(window)
image_label.pack(pady=10)

watermark_entry = tk.Entry(window, width=30)
watermark_entry.pack(pady=10)
watermark_entry.insert(0, "Enter watermark text")

watermark_button = tk.Button(window, text="Add Watermark", command=add_watermark)
watermark_button.pack(pady=10)

window.mainloop()
