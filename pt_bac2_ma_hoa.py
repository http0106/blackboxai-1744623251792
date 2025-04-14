import tkinter as tk
from tkinter import ttk
import math

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng Giải PT bậc 2 & Mã hóa")
        self.geometry("500x400")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self)
        
        # Quadratic equation solver tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Giải PT bậc 2")
        self.setup_quadratic_tab()
        
        # Encryption tab
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Mã hóa dữ liệu")
        self.setup_encryption_tab()
        
        self.notebook.pack(expand=True, fill="both")

    def setup_quadratic_tab(self):
        # Input fields
        tk.Label(self.tab1, text="Nhập hệ số a:").pack()
        self.a_entry = tk.Entry(self.tab1)
        self.a_entry.pack()
        
        tk.Label(self.tab1, text="Nhập hệ số b:").pack()
        self.b_entry = tk.Entry(self.tab1)
        self.b_entry.pack()
        
        tk.Label(self.tab1, text="Nhập hệ số c:").pack()
        self.c_entry = tk.Entry(self.tab1)
        self.c_entry.pack()
        
        # Solve button
        tk.Button(self.tab1, text="Giải phương trình", command=self.solve_quadratic).pack(pady=10)
        
        # Result display
        self.result_label = tk.Label(self.tab1, text="", fg="blue")
        self.result_label.pack()

    def solve_quadratic(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            
            delta = b**2 - 4*a*c
            
            if delta < 0:
                result = "Phương trình vô nghiệm"
            elif delta == 0:
                x = -b/(2*a)
                result = f"Phương trình có nghiệm kép x = {x:.2f}"
            else:
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                result = f"Phương trình có 2 nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}"
                
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Vui lòng nhập hệ số hợp lệ!", fg="red")

    def setup_encryption_tab(self):
        # Input fields
        tk.Label(self.tab2, text="Nhập văn bản:").pack()
        self.text_entry = tk.Text(self.tab2, height=5)
        self.text_entry.pack()
        
        tk.Label(self.tab2, text="Nhập khóa (số nguyên):").pack()
        self.key_entry = tk.Entry(self.tab2)
        self.key_entry.pack()
        
        # Buttons
        button_frame = tk.Frame(self.tab2)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Mã hóa", command=self.encrypt).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Giải mã", command=self.decrypt).pack(side=tk.LEFT, padx=5)
        
        # Result display
        self.encryption_result = tk.Text(self.tab2, height=5, state="disabled")
        self.encryption_result.pack()

    def encrypt(self):
        self.process_text(encrypt=True)

    def decrypt(self):
        self.process_text(encrypt=False)

    def process_text(self, encrypt=True):
        try:
            text = self.text_entry.get("1.0", tk.END).strip()
            key = int(self.key_entry.get())
            
            result = []
            for char in text:
                if char.isalpha():
                    shift = key if encrypt else -key
                    if char.isupper():
                        result.append(chr((ord(char) - 65 + shift) % 26 + 65))
                    else:
                        result.append(chr((ord(char) - 97 + shift) % 26 + 97))
                else:
                    result.append(char)
            
            self.encryption_result.config(state="normal")
            self.encryption_result.delete("1.0", tk.END)
            self.encryption_result.insert("1.0", "".join(result))
            self.encryption_result.config(state="disabled")
        except ValueError:
            self.encryption_result.config(state="normal")
            self.encryption_result.delete("1.0", tk.END)
            self.encryption_result.insert("1.0", "Vui lòng nhập khóa hợp lệ!")
            self.encryption_result.config(state="disabled")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
