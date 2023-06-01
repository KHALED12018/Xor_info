import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

def open_binary_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as file:
        content = file.read()
    return content, file_path

def find_most_frequent_bytes(content):
    byte_count = Counter(content)
    sorted_bytes = sorted(byte_count.items(), key=lambda x: x[1], reverse=True)
    most_frequent_bytes = [byte for byte, count in sorted_bytes if byte != 0x00]
    return most_frequent_bytes

def xor_file(content, xor_byte):
    xor_result = bytes([byte ^ xor_byte for byte in content])
    return xor_result

def save_file(xor_result):
    save_path = filedialog.asksaveasfilename(defaultextension=".bin")
    with open(save_path, 'wb') as file:
        file.write(xor_result)

def open_file_button_clicked():
    content, file_path = open_binary_file()
    most_frequent_bytes = find_most_frequent_bytes(content)

    file_path_label.config(text="File Path: " + file_path)

    result_frame = tk.Frame(root, bd=2, relief="groove")
    result_frame.pack(pady=10)

    result_label = tk.Label(result_frame, text="Most Frequent Bytes", font=("Helvetica", 14, "bold"))
    result_label.pack()

    for byte in most_frequent_bytes:
        byte_label = tk.Label(result_frame, text=hex(byte), font=("Helvetica", 12))
        byte_label.pack()
    xor_button = tk.Button(xor_frame, text="XOR and Save", command=lambda: xor_and_save(content, xor_entry.get()))
    xor_button.pack()

def xor_and_save(content, xor_value):
    try:
        xor_byte = int(xor_value, 16)
        xor_result = xor_file(content, xor_byte)
        save_file(xor_result)
        messagebox.showinfo("XOR Result", "XOR operation completed and file saved successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid XOR value. Please enter a valid hexadecimal value.")

root = tk.Tk()
root.title("Xor_File_Info by DragnNoir2023")
root.geometry("400x400")

file_path_label = tk.Label(root, text="File Path: ")
file_path_label.pack()

open_file_button = tk.Button(root, text="Open File", command=open_file_button_clicked)
open_file_button.pack()

xor_frame = tk.Frame(root, bd=2, relief="groove")
xor_frame.pack(pady=10)

xor_label = tk.Label(xor_frame, text="XOR Value", font=("Helvetica", 14, "bold"))
xor_label.pack()

xor_entry = tk.Entry(xor_frame, font=("Helvetica", 12))
xor_entry.pack()

root.mainloop()
