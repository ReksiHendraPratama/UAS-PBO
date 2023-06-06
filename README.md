# UAS-PBO
# ANGGOTA KELOMPOK
1. REKSI HENDRA PRATAMA
2. PANDU RIZKI MULYANTO
3. WAHYU OZORAH MANURUNG

# PENJELASAN SOURCE CODE
# IMPORT
Pada bagian ini merupakan bagian module untuk membuat tkinter, yang mana berisikan library dengan mengimpor semua dari tkinter
```
from tkinter import *  # Mengimpor semua dari modul tkinter
from tkinter.filedialog import asksaveasfile, askopenfile # Mengimpor fungsi asksaveasfile() dan askopenfile() dari modul filedialog
from tkinter import colorchooser # Mengimpor modul colorchooser dari tkinter
from tkinter import font as tkfont #mengimpor font sesuai demgam jemis 
from tkinter import simpledialog #mengimpor untuk font 
```

# Class Notepad
Pada bagian ini merupakan kode untuk membuat class notepad yang mana pertama membuat untuk window dengan menyimpan jendela utama. selanjutnya menetapkan judul pada note pada dengan judul "notepad" dengan ukuran window yaitu sebesar 1200*600 piksel. selanjutnya membuat row dengan configure nya yaitu 0 sebagai tata letak nya. kemudian membuat area teks dalam menulis kata katanya serta ada fungsi untuk membuat menu-menu yang menjadi bagian pada notepad
```
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
```

# Create Menu File
Pada kode ini menjelaskan proses pembuatan menu file yang mana pada menu file terdapat sub menu yaitu new, open, save. yang mana new itu membuat kertas/ area baru, open untuk membuka file, save untuk menyimpan file dalam bentuk txt. Adapun kode nya sebagai berikut.
```
     def create_menu(self):
            Daftar_menu = Menu(self.window) # Membuat objek menu utama

            file_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu file dengan submenu
            file_menu.add_command(label="New", command=self.new_file) # Menambahkan perintah "New" ke submenu file
            file_menu.add_command(label="Open", command=self.open_file) # Menambahkan perintah "Open" ke submenu file
            file_menu.add_command(label="Save", command=self.save_file) # Menambahkan perintah "Save" ke submenu file
            file_menu.add_separator() # Menambahkan pemisah ke submenu file
            Daftar_menu.add_cascade(label="File", menu=file_menu) # Menambahkan submenu file ke menu utama
```

# Create Menu edit
Pada kode ini menjelaskan proses pembuatan menu untuk edit file yang mana pada menu ini terdapat sub menu cut untuk memotong teks, copy untuk mengcopy teks serta pase untuk me pastekan text yang di copy. Adapun code nya sebagai berikut.
```
   edit_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu edit dengan submenu
        edit_menu.add_command(label="Cut", command=self.cut_text) # Menambahkan perintah "Cut" ke submenu edit
        edit_menu.add_command(label="Copy", command=self.copy_text) # Menambahkan perintah "Copy" ke submenu edit
        edit_menu.add_command(label="Paste", command=self.paste_text) # Menambahkan perintah "Paste" ke submenu edit
        Daftar_menu.add_cascade(label="Edit", menu=edit_menu) # Menambahkan submenu edit ke menu utama
 ```
 
 # Create Menu Format
Pada bagian ini menjelaskan menu untuk membuat format tulisan nya yang mana tulisannya bisa diubah menjadi sesuai font yang kita mau sedangkan size nya juga sesuai dengan yang kita mau. dengan memasukkan jenis font maka font dari tulisan akan berubah dengan memasukkan angka size untuk font maka size nya akan berubah juga.
```
format_menu = Menu(Daftar_menu, tearoff=0)
    format_menu.add_command(label="Font", command=self.change_font)
    format_menu.add_command(label="Font Size", command=self.change_font_size)
    Daftar_menu.add_cascade(label="Format", menu=format_menu)
 ```
 
 # Create Menu Color
Pada bagian ini untuk membuat color dari area tulisan. Pada menu ini user akan bebas mengganti warna yang akan digunakan sesuai dengan keinginannya dan warna kesukaannya.
```
color_menu = Menu(Daftar_menu, tearoff=0) # Membuat menu warna dengan submenu
    color_menu.add_command(label="Change Color", command=self.change_color) # Menambahkan perintah "Change Color" ke submenu warna
    Daftar_menu.add_cascade(label="Color", menu=color_menu) # Menambahkan submenu warna ke menu utama
 ```

# Create Menu Exit
Pada bagian ini untuk membuat menu yang menghasilkan keluar atau menutup program nya ketika di klik. Untuk code nya sebagai berikut. 
```
 Daftar_menu.add_cascade(label="Exit", command=self.window.quit) # Menambahkan perintah "Exit" ke menu utama
    self.window.config(menu=Daftar_menu) # Mengonfigurasi menu jendela dengan daftar menu yang telah dibuat
```
        
# Membuat Fungsi untuk Menghapus Area Teks
Pada bagian menu hapus kode akan berjalan dengan fungsi sebagai berikut
```
    def new_file(self): # Menghapus isi area teks
        self.text_area.delete(1.0, END)
```

# Membuat Fungsi untuk Membuka File
Pada bagian open file fungsi yang digunakan untuk kode bisa berjalan sebagai berikut
``` 
  def open_file(self): # Memunculkan  membuka file
    file = askopenfile(mode="r", filetypes=[('Text Files', '*.txt')])
    if file is not None:
        content = file.read() # Membaca isi file
        self.text_area.delete(1.0, END) # Menghapus isi area teks
        self.text_area.insert(END, content) # Menyisipkan isi file ke area teks
        file.close() # Menutup file
```

# Membuat Menu untuk Save File
Pada bagian ini fungsi untuk me save file yang dibuat adalah sebagai berikut. 
```
      def save_file(self):
        file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[('Text Files', '*.txt')]) # Memunculkan dialog penyimpanan file
        if file is not None:
            text = self.text_area.get(1.0, END) # Mendapatkan teks dari area teks
            file.write(text) # Menulis teks ke file
            file.close() # Menutup file
```

# Fungsi untuk Memotong Teks
```
        def cut_text(self):
        self.text_area.event_generate("<<Cut>>") # Memanggil perintah cut pada area teks
```

# Fungsi untuk Mengcopy Teks
```
    def copy_text(self):
    self.text_area.event_generate("<<Copy>>") # Memanggil perintah copy pada area teks
```

# Fungsi untuk Melakukan Paste pada Teks
```
    def paste_text(self):
    self.text_area.event_generate("<<Paste>>") # Memanggil perintah paste pada area teks
```

# Fungsi untuk Mengatur Warna pada Menu Color
```
    def change_color(self):
    color = colorchooser.askcolor() # Memunculkan dialog pemilih warna
    if color[1] is not None:
        self.text_area.config(bg=color[1]) # Mengubah warna latar belakang area teks
```

# Fungsi untuk Mengatur Jenis Font dan Ukuran Font
```
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
```

# Fungsi untuk Menjalankan Keseluruhan Kode Agar Bisa Memunculkan Notepadnya
```
         if __name__ == "__main__":
            window = Tk()  # Membuat objek jendela
            notepad = Notepad(window) # Membuat objek Notepad dengan jendela sebagai argumen
            window.mainloop() # Menjalankan loop utama jendela
```

# Penjelasan secara Keseluruhan
Pada dasarnya seluruh kode digunakan untuk membuat sebuah notepad. Notepad dibuat sesuai dengan menu yang ada dengan menggunakan bahasa python dan bantuan tkinter hingga dihasilkan notepad.
