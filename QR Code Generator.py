import tkinter as tk
from tkinter import messagebox, colorchooser, filedialog
import qrcode
from PIL import Image, ImageTk

# Main window class
class QRCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.english_text = {
            "language_label": "Language:",
            "url_label": "URL:",
            "bg_color_label": "Background Color",
            "qr_color_label": "QR Code Color",
            "preview_label": "Preview",
            "save_button": "Save",
            "edit_color_button": "Edit Color",
            "cancel_button": "Cancel",
            "chinese_rb": "Chinese (simplified)",
            "english_rb": "English",
            "quantity_label": "Quantity"
        }

        self.chinese_text = {
            "language_label": "语言:",
            "url_label": "网址:",
            "bg_color_label": "背景颜色",
            "qr_color_label": "二维码颜色",
            "preview_label": "预览",
            "save_button": "保存",
            "edit_color_button": "编辑颜色",
            "cancel_button": "取消",
            "chinese_rb": "简体中文",
            "english_rb": "英文",
            "quantity_label": "数量"
        }

        self.title('QR Code Generator')
        self.geometry('500x500')

        # Set initial language
        self.current_language = self.english_text

        # Language Selection
        self.language_var = tk.StringVar(value="English")

        self.language_label = tk.Label(self, text=self.current_language["language_label"])
        self.language_label.grid(row=0, column=0, sticky="w")

        self.chinese_rb = tk.Radiobutton(self, text=self.current_language["chinese_rb"],
                                         variable=self.language_var, value="Chinese",
                                         command=self.switch_language)
        self.chinese_rb.grid(row=0, column=1)

        self.english_rb = tk.Radiobutton(self, text=self.current_language["english_rb"],
                                         variable=self.language_var, value="English",
                                         command=self.switch_language)
        self.english_rb.grid(row=0, column=2)

        # URL Entry
        self.url_label = tk.Label(self, text=self.current_language["url_label"])
        self.url_label.grid(row=1, column=0, sticky="w")

        self.url_entry = tk.Entry(self)
        self.url_entry.grid(row=1, column=1, columnspan=2, sticky="we")
        self.url_entry.bind("<KeyRelease>", self.generate_preview)

        # Color Selection
        self.bg_color_var = tk.StringVar(value="white")
        self.qr_color_var = tk.StringVar(value="black")

        # Background Color Button
        self.bg_color_label = tk.Label(self, text=self.current_language["bg_color_label"])
        self.bg_color_label.grid(row=2, column=0, sticky="w")

        self.bg_color_button = tk.Button(self, bg=self.bg_color_var.get(), width=2,
                                         command=lambda: self.choose_color(self.bg_color_var))
        self.bg_color_button.grid(row=2, column=1, sticky="we")

        # QR Code Color Button
        self.qr_color_label = tk.Label(self, text=self.current_language["qr_color_label"])
        self.qr_color_label.grid(row=3, column=0, sticky="w")

        self.qr_color_button = tk.Button(self, bg=self.qr_color_var.get(), width=2,
                                         command=lambda: self.choose_color(self.qr_color_var))
        self.qr_color_button.grid(row=3, column=1, sticky="we")

        # Preview Label (placeholder for the QR code image)
        self.preview_label = tk.Label(self, text=self.current_language["preview_label"])
        self.preview_label.grid(row=4, column=0, columnspan=3)

        # Save Button
        self.save_button = tk.Button(self, text=self.current_language["save_button"], command=self.save_qr_code)
        self.save_button.grid(row=5, column=1, sticky="we")

        # Quantity Entry
        self.quantity_label = tk.Label(self, text=self.current_language["quantity_label"])
        self.quantity_label.grid(row=6, column=0, sticky="w")

        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(row=6, column=1, columnspan=2, sticky="we")
        self.quantity_entry.insert(0, "1")  # Default quantity

    def switch_language(self):
        # Switch the language text and update labels/buttons
        language = self.language_var.get()
        self.current_language = self.chinese_text if language == "Chinese" else self.english_text
        self.language_label.config(text=self.current_language["language_label"])
        self.url_label.config(text=self.current_language["url_label"])
        self.bg_color_label.config(text=self.current_language["bg_color_label"])
        self.qr_color_label.config(text=self.current_language["qr_color_label"])
        self.save_button.config(text=self.current_language["save_button"])
        self.preview_label.config(text=self.current_language["preview_label"])
        self.chinese_rb.config(text=self.current_language["chinese_rb"])
        self.english_rb.config(text=self.current_language["english_rb"])
        self.quantity_label.config(text=self.current_language["quantity_label"])
        self.generate_preview()

    def generate_preview(self, event=None):
        # Generate QR code preview with the current URL and selected colors
        data = self.url_entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color=self.qr_color_var.get(), back_color=self.bg_color_var.get())

            # Get the current size of the preview label to resize the QR code accordingly
            current_preview_size = (self.preview_label.winfo_width(), self.preview_label.winfo_height())
            min_size = (160, 160)  # Adjust as needed to fit your GUI layout
            target_size = max(current_preview_size, min_size)

            # Instead of thumbnail, resized image to target size using best resampling filter
            img = img.resize(target_size, Image.Resampling.LANCZOS)

            self.qr_img = ImageTk.PhotoImage(img)
            self.preview_label.config(image=self.qr_img, text="")  # Remove text and set image
        else:
            self.preview_label.config(image='', text=self.current_language["preview_label"])  # No data, show text

    def choose_color(self, color_var):
        # Open a color dialog and set the selected color to the button and variable
        color = colorchooser.askcolor()[1]
        if color:
            color_var.set(color)
            if color_var == self.bg_color_var:
                self.bg_color_button.config(bg=color)
            elif color_var == self.qr_color_var:
                self.qr_color_button.config(bg=color)

            # Generate a new preview with the updated colors
            self.generate_preview()

    def save_qr_code(self):
        base_data = self.url_entry.get()
        if base_data:
            try:
                quantity = int(self.quantity_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid quantity.")
                return

            base_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if not base_file_path:
                # 用户取消了保存操作
                return

            for i in range(quantity):
                # 在原始文本后添加不同数量的空格
                unique_data = base_data + " " * (i + 1)

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(unique_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color=self.qr_color_var.get(), back_color=self.bg_color_var.get())

                file_path = f"{base_file_path}_{i+1}.png"
                img.save(file_path)

            messagebox.showinfo("Success", f"{quantity} QR Codes saved successfully.")
        else:
            messagebox.showerror("Error", "No base data to encode.")

# Run the application
if __name__ == "__main__":
    app = QRCodeGenerator()
    app.mainloop()