import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *



def way():
    global scan_dir_to_encrypt_decrypt
    scan_dir_to_encrypt_decrypt = txt.get()
    key()

def key():
    key = Fernet.generate_key()
    if not os.path.exists('my_key.txt'):
        with open('my_key.txt', 'wb') as f:
            f.write(key)
    else:
        key = open('my_key.txt', 'rb').read()
    print(key)
    global cipher
    cipher = Fernet(key)

def encrypt():
    global encrypt_yes
    encrypt_yes = True

def decrypt():
    global encrypt_yes
    encrypt_yes = False

def start():
    if encrypt_yes:
        with os.scandir(path=scan_dir_to_encrypt_decrypt) as it:
            for entry in it:
                if not entry.is_file():
                    print("dir:\t" + entry.name)
                else:
                    read_file = open(scan_dir_to_encrypt_decrypt+entry.name, 'rb').read()
                    encrypted_file_content = cipher.encrypt(read_file)
                    with open(scan_dir_to_encrypt_decrypt+entry.name, 'wb') as f:
                        f.write(encrypted_file_content)
                    print("file encrypted:\t" + entry.name)
    else:
        with os.scandir(path=scan_dir_to_encrypt_decrypt) as it:
            for entry in it:
                if not entry.is_file():
                    print("dir:\t" + entry.name)
                else:
                    encrypted_file_content = open(scan_dir_to_encrypt_decrypt+entry.name, 'rb').read()
                    file_content = cipher.decrypt(encrypted_file_content)
                    with open(scan_dir_to_encrypt_decrypt+entry.name, 'wb') as f:
                        f.write(file_content)
                    print("file decrypted:\t" + entry.name)

window = tk.Tk()
window.title("Шифровальщик")
window.geometry('400x250')
window.iconbitmap(r'C:\Users\cerec\OneDrive\Рабочий стол\cryptography\icon.ico')

txt = Entry(window, width=25)
txt.grid(column=0, row=0)

way_btn = Button(window, text="записать путь", command = way)
way_btn.grid(column=2, row = 0)

encrypt_btn = Button(window, text="зашифровать", command = encrypt)
encrypt_btn.grid(column=0, row = 1)

start_btn = Button(window, text="запустить", command = start)
start_btn.grid(column=1, row = 2)

decrypt_btn = Button(window, text="расшифровать", command = decrypt)
decrypt_btn.grid(column=2, row = 1)

window.mainloop()
