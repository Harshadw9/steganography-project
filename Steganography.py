import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import stepic

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography App")
        self.root.geometry("500x400")

        self.image_label = tk.Label(self.root, text="No Image Selected", width=50)
        self.image_label.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select Image", command=self.load_image)
        self.select_button.pack()

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)
        self.message_entry.insert(0, "Enter secret message")

        self.encode_button = tk.Button(self.root, text="Encode Message", command=self.encode_image)
        self.encode_button.pack()

        self.decode_button = tk.Button(self.root, text="Decode Message", command=self.decode_image)
        self.decode_button.pack()

        self.image_path = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img.thumbnail((200, 200))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img, text="")
            self.image_label.image = img

    def encode_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected")
            return
        
        secret_message = self.message_entry.get()
        image = Image.open(self.image_path)
        encoded_image = stepic.encode(image, secret_message.encode())
        encoded_image.save("encoded_image.png", "PNG")
        messagebox.showinfo("Success", "Message encoded and saved as encoded_image.png")

    def decode_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected")
            return
        
        image = Image.open(self.image_path)
        hidden_message = stepic.decode(image)
        messagebox.showinfo("Decoded Message", hidden_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
