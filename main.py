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

        subprocess.Popen(["pingFiliais.bat"])
        print(subprocess)
    
    else:
        messagebox.showerror("Filial inválida", "Por gentileza, verifique a filial!")


    
    


def pingGang():
    filial = numeroFilial.get()

    os.environ["filial"] = filial
    os.environ["tipoFilial"] = "Gang"

    subprocess.Popen(["pingFiliais.bat"])
    print(subprocess)
    


# inicializar janela main
root = tk.Tk()
root.title("Ping filiais Lins Ferrão")
style = Style(theme='cyborg')
root.iconbitmap("icon.ico")
root.minsize(500, 400)
root.maxsize(500, 400)
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)  


# preciso que seja recebido uma variável com a loja e ser pingada
# número e botão.

# configurações da página

texto = ttk.Label(root, text="Ping Filiais")
texto.grid(row=1, column=4)

textoNumeroFilial = ttk.Label(root, text="Filial", padding=2)
textoNumeroFilial.grid(row=2, column=3)
numeroFilial = ttk.Entry(root)
numeroFilial.grid(row=2, column=4)

botaoPompeia = ttk.Button(root, text="Ping Pompéia", command=pingPompeia, width=20, style="secondary.TButton")
botaoPompeia.grid(row=4, column=3, padx=3, pady=3)

botaoGang = ttk.Button(root, text="Ping Gang", command=pingGang, width=20, style="Secondary.TButton")
botaoGang.grid(row=4, column=6)

#imagem = tk.PhotoImage(file=)



root.mainloop()
