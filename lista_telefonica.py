import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

contatos = [
    {"nome": "Ana Silva", "telefone": "(11) 99999-1111"},
    {"nome": "Bruno Souza", "telefone": "(21) 98888-2222"},
    {"nome": "Carlos Lima", "telefone": "(31) 97777-3333"},
    {"nome": "Daniela Rocha", "telefone": "(41) 96666-4444"},
    {"nome": "Eduardo Alves", "telefone": "(51) 95555-5555"}
]

def buscar_contatos():
    termo = entrada_busca.get().lower()
    for widget in lista_frame.winfo_children():
        widget.destroy()
    for contato in contatos:
        if termo in contato["nome"].lower():
            criar_card(contato)

def criar_card(contato):
    card = ttk.Frame(lista_frame, style="Card.TFrame", padding=10)
    card.pack(pady=5, padx=20, fill="x")
    img_label = tk.Label(card, image=img_contato)
    img_label.pack(side="left", padx=10)
    info_frame = ttk.Frame(card)
    info_frame.pack(side="left", fill="x", expand=True)
    nome_label = ttk.Label(info_frame, text=contato["nome"], font=("Arial", 14, "bold"))
    nome_label.pack(anchor="w")
    telefone_label = ttk.Label(info_frame, text=contato["telefone"], font=("Arial", 12))
    telefone_label.pack(anchor="w")

janela = tk.Tk()
janela.title("Lista Telefônica")
janela.geometry("900x700")
janela.configure(bg="#dbd8d8")

style = ttk.Style()
style.configure("Card.TFrame", background="#f0f0f0", relief="raised", borderwidth=1)

titulo = tk.Label(janela, text="Lista Telefônica", font=("Arial", 30), bg="#dbd8d8")
titulo.pack(pady=20)

busca_frame = tk.Frame(janela, bg="#f0f0f0")
busca_frame.pack()

entrada_busca = tk.Entry(busca_frame, font=("Arial", 12), width=40)
entrada_busca.pack(side="left", padx=10, ipady=5)

botao_buscar = tk.Button(busca_frame, text="Buscar", command=buscar_contatos, bg="#4CAF50", fg="white", padx=20, pady=5)
botao_buscar.pack(side="left")

lista_frame = tk.Frame(janela, bg="#dbd8d8")
lista_frame.pack(pady=20, fill="both", expand=True)

try:
    imagem = Image.open("imagem/person.png").resize((60, 60))
except FileNotFoundError:
    imagem = Image.new("RGB", (60, 60), color="gray")
img_contato = ImageTk.PhotoImage(imagem)

for contato in contatos:
    criar_card(contato)

janela.mainloop()
