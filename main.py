import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import os
import subprocess

def pingPompeia():
    filial = numeroFilial.get()

    if len(filial) > 0 and len(filial) < 3:    
        os.environ["filial"] = filial
        os.environ["tipoFilial"] = "Pompeia"

        subprocess.Popen(["_internal/pingFiliais.bat"])
        
    else:
        messagebox.showerror("Filial inválida", "Por gentileza, verifique a filial!")



def pingGang():
    filial = numeroFilial.get()

    if len(filial) > 0 and len(filial) < 3:
        os.environ["filial"] = filial
        os.environ["tipoFilial"] = "Gang"

        subprocess.Popen(["_internal/pingFiliais.bat"])

    else:
        messagebox.showerror("Filial inválida", "Por gentileza, verifique a filial!")
        
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")      


# inicializar janela main
root = tk.Tk()
root.title("Ping Filiais")
style = Style(theme='cyborg')
root.minsize(300, 200)
root.maxsize(500, 400)


# Centraliza as 3 primeiras linhas
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Primeira linha: Texto "Ping Filiais"
texto = ttk.Label(root, text="Ping Filiais", font=("Arial", 16))
texto.grid(row=0, column=0, columnspan=4, pady=10)

# Segunda linha: Texto "Filial"
textoNumeroFilial = ttk.Label(root, text="Filial", font=("Arial", 12))
textoNumeroFilial.grid(row=1, column=0, columnspan=4, pady=5)

# Terceira linha: Campo Entry para número da filial
numeroFilial = ttk.Entry(root, font=("Arial", 12))
numeroFilial.grid(row=2, column=0, columnspan=4, pady=5)

# Quarta linha: Botões "Ping Pompéia" e "Ping Gang" lado a lado
botaoPompeia = ttk.Button(root, text="Ping Pompéia", command=pingPompeia, width=20, style="secondary.TButton")
botaoPompeia.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky='ew')

botaoGang = ttk.Button(root, text="Ping Gang", command=pingGang, width=20, style="Secondary.TButton")
botaoGang.grid(row=3, column=2, columnspan=2, padx=5, pady=10, sticky='ew')

# Configura o espacamento entre as colunas
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.after(1, center_window, root)

root.mainloop()
