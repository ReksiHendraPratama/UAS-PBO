from tkinter import *  # Mengimpor semua dari modul tkinter
from tkinter.filedialog import asksaveasfile, askopenfile # Mengimpor fungsi asksaveasfile() dan askopenfile() dari modul filedialog
from tkinter import colorchooser # Mengimpor modul colorchooser dari tkinter
from tkinter import font as tkfont #mengimpor font sesuai demgam jemis 
from tkinter import simpledialog #mengimpor untuk font

class Notepad:
    def __init__(self, window): #Fungsi untuk window
        self.window = window # Menyimpan objek jendela utama
        self.window.title("MyNotepad") # Menetapkan judul jendela menjadi "Notepad"
        self.window.geometry("1200x600")  # Menetapkan ukuran jendela menjadi 1200x600 piksel

        window.rowconfigure(0, weight=1) # Mengkonfigurasi tata letak baris untuk mengisi ruang yang tersedia
        window.columnconfigure(0, weight=1) # Mengkonfigurasi tata letak kolom untuk mengisi ruang yang tersedia

        self.text_area = Text(self.window, wrap=WORD) # Membuat area teks dalam jendela dengan pembungkus kata
        self.text_area.pack(expand=True, fill=BOTH) # Mengemas area teks agar memanfaatkan seluruh ruang yang tersedia dalam jendela dalam membuat teks

        self.create_menu() # Membuat menu

    def create_menu(self):
        Daftar_menu = Menu(self.window) # Membuat objek menu utama

        file_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu file dengan submenu
        file_menu.add_command(label="New", command=self.new_file) # Menambahkan perintah "New" ke submenu file
        file_menu.add_command(label="Open", command=self.open_file) # Menambahkan perintah "Open" ke submenu file
        file_menu.add_command(label="Save", command=self.save_file) # Menambahkan perintah "Save" ke submenu file
        file_menu.add_separator() # Menambahkan pemisah ke submenu file
        Daftar_menu.add_cascade(label="File", menu=file_menu) # Menambahkan submenu file ke menu utama

        edit_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu edit dengan submenu
        edit_menu.add_command(label="Cut", command=self.cut_text) # Menambahkan perintah "Cut" ke submenu edit
        edit_menu.add_command(label="Copy", command=self.copy_text) # Menambahkan perintah "Copy" ke submenu edit
        edit_menu.add_command(label="Paste", command=self.paste_text) # Menambahkan perintah "Paste" ke submenu edit
        Daftar_menu.add_cascade(label="Edit", menu=edit_menu) # Menambahkan submenu edit ke menu utama

        format_menu = Menu(Daftar_menu, tearoff=0)
        format_menu.add_command(label="Font", command=self.change_font)
        format_menu.add_command(label="Font Size", command=self.change_font_size)
        Daftar_menu.add_cascade(label="Format", menu=format_menu)

        color_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu warna dengan submenu
        color_menu.add_command(label="Change Color", command=self.change_color) # Menambahkan perintah "Change Color" ke submenu warna
        Daftar_menu.add_cascade(label="Color", menu=color_menu) # Menambahkan submenu warna ke menu utama

        Daftar_menu.add_cascade(label="Exit", command=self.window.quit) # Menambahkan perintah "Exit" ke menu utama

        self.window.config(menu=Daftar_menu) # Mengonfigurasi menu jendela dengan daftar menu yang telah dibuat

    def new_file(self): # Menghapus isi area teks
        self.text_area.delete(1.0, END)

    def open_file(self): # Memunculkan dialog membuka file
        file = askopenfile(mode="r", filetypes=[('Text Files', '*.txt')])
        if file is not None:
            content = file.read() # Membaca isi file
            self.text_area.delete(1.0, END) # Menghapus isi area teks
            self.text_area.insert(END, content) # Menyisipkan isi file ke area teks
            file.close() # Menutup file

    def save_file(self):
        file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[('Text Files', '*.txt')]) # Memunculkan dialog penyimpanan file
        if file is not None:
            text = self.text_area.get(1.0, END) # Mendapatkan teks dari area teks
            file.write(text) # Menulis teks ke file
            file.close() # Menutup file

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>") # Memanggil perintah cut pada area teks

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>") # Memanggil perintah copy pada area teks

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>") # Memanggil perintah paste pada area teks

    def change_color(self):
        color = colorchooser.askcolor() # Memunculkan dialog pemilih warna
        if color[1] is not None:
            self.text_area.config(bg=color[1]) # Mengubah warna latar belakang area teks

    def change_font_size(self):
        size = simpledialog.askinteger("Font Size", "Enter font size:") #untuk font size
        if size:
            font = tkfont.Font(self.text_area, self.text_area.cget("font")) #mengganti size di area notepad
            font.configure(size=size) #font size
            self.text_area.configure(font=font) 
        
    def change_font(self): #untuk menukar font
        family = simpledialog.askstring("Font Family", "Enter font family:") #jenis font yang akan diganti
        if family:
            font = tkfont.Font(self.text_area, self.text_area.cget("font")) 
            font.configure(family=family)
            self.text_area.configure(font=font)

if __name__ == "__main__":
    window = Tk()  # Membuat objek jendela
    notepad = Notepad(window) # Membuat objek Notepad dengan jendela sebagai argumen
    window.mainloop() # Menjalankan loop utama jendela