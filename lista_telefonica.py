import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys

# ======================= CONFIGURAÇÃO DPI =======================
# Habilita a consciência de DPI no Windows para evitar interface borrada
if sys.platform == "win32":
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass


def get_dpi_scale():
    """Obtém o fator de escala DPI para o display"""
    try:
        if sys.platform == "win32":
            from ctypes import windll

            dc = windll.user32.GetDC(0)
            dpi = windll.gdi32.GetDeviceCaps(dc, 88)  # LOGPIXELSX
            windll.user32.ReleaseDC(0, dc)
            return dpi / 96.0  # 96 DPI é 100% de escala
        else:
            # Para outras plataformas, assume escala 1.0
            return 1.0
    except Exception:
        return 1.0


def scale_size(size, scale_factor=None):
    """Escala um valor de tamanho baseado no DPI"""
    if scale_factor is None:
        scale_factor = get_dpi_scale()
    return int(size * scale_factor)


# ======================= DADOS =======================
# Lista de contatos que será exibida na interface
contatos = [
    {"nome": "Ana Silva", "telefone": "(11) 99999-1111"},
    {"nome": "Bruno Souza", "telefone": "(21) 98888-2222"},
    {"nome": "Carlos Lima", "telefone": "(31) 97777-3333"},
    {"nome": "Daniela Rocha", "telefone": "(41) 96666-4444"},
    {"nome": "Eduardo Alves", "telefone": "(51) 95555-5555"},
]

# ======================= CONSTANTES =======================
BG_COLOR = "#FFFFFF"  # Cor de fundo da aplicação
DPI_SCALE = get_dpi_scale()  # Fator de escala DPI obtido na inicialização


# ======================= FUNÇÕES =======================
def buscar_contatos():
    """Filtra e exibe contatos baseado no termo de busca"""
    termo = entrada_busca.get().lower()

    # Remove todos os cards existentes da lista
    for widget in lista_frame.winfo_children():
        widget.destroy()

    # Cria cards apenas para contatos que contêm o termo de busca
    for contato in contatos:
        if termo in contato["nome"].lower():
            criar_card(contato)


def criar_card(contato):
    """Cria um card visual para exibir informações do contato"""
    # Frame principal do card com estilo personalizado
    card = ttk.Frame(lista_frame, style="Card.TFrame", padding=scale_size(5, DPI_SCALE))
    card.pack(pady=scale_size(5, DPI_SCALE), padx=scale_size(5, DPI_SCALE), fill="x")

    # Imagem do contato (lado esquerdo)
    img_label = tk.Label(card, image=img_contato)
    img_label.pack(side="left", padx=scale_size(10, DPI_SCALE))

    # Frame para informações do contato (lado direito)
    info_frame = ttk.Frame(card)
    info_frame.pack(side="left", fill="x", expand=True)

    # Label com o nome do contato
    nome_label = ttk.Label(
        info_frame,
        text=contato["nome"],
        font=("Segoe UI", scale_size(14, DPI_SCALE), "normal"),
    )
    nome_label.pack(anchor="w")

    # Label com o telefone do contato
    telefone_label = ttk.Label(
        info_frame,
        text=contato["telefone"],
        font=("Segoe UI", scale_size(12, DPI_SCALE)),
    )
    telefone_label.pack(anchor="w")


# ======================= JANELA PRINCIPAL =======================
# Criação da janela principal
janela = tk.Tk()
janela.title("Lista Telefônica")

# Configuração do tamanho da janela baseado no DPI
window_width = scale_size(900, DPI_SCALE)
window_height = scale_size(700, DPI_SCALE)
janela.geometry(f"{window_width}x{window_height}")
janela.configure(bg=BG_COLOR)

# Configura o tkinter para usar escala DPI
janela.tk.call("tk", "scaling", DPI_SCALE)

# ======================= ESTILOS =======================
# Definição de tamanhos de fonte escalados
title_font_size = scale_size(30, DPI_SCALE)
entry_font_size = scale_size(12, DPI_SCALE)

# Estilo personalizado para os cards dos contatos
style = ttk.Style()
style.configure("Card.TFrame", background="#f0f0f0", relief="flat", borderwidth=1)

# ======================= TÍTULO =======================
# Título principal da aplicação (topo da tela)
titulo = tk.Label(
    janela, text="Lista Telefônica", font=("Segoe UI", title_font_size), bg=BG_COLOR
)
titulo.pack(pady=scale_size(20, DPI_SCALE))

# ======================= BARRA DE BUSCA =======================
# Frame contenedor da barra de busca
busca_frame = tk.Frame(janela, bg="#ffffff", border=1, borderwidth=2, relief="groove")
busca_frame.pack()

# Campo de entrada de texto para busca
entrada_busca = tk.Entry(
    busca_frame, font=("Segoe UI", entry_font_size), border=0, width=40
)
entrada_busca.pack(
    side="left", padx=scale_size(10, DPI_SCALE), ipady=scale_size(5, DPI_SCALE)
)

# Botão para executar a busca
botao_buscar = tk.Button(
    busca_frame,
    text="Buscar",
    command=buscar_contatos,
    bg="#4CAF50",
    border=0,
    fg="white",
    font=("Segoe UI", entry_font_size),
    padx=scale_size(20, DPI_SCALE),
    pady=scale_size(5, DPI_SCALE),
)
botao_buscar.pack(side="left")

# ======================= LISTA DE CONTATOS =======================
# Frame contenedor da lista de contatos
lista_frame = tk.Frame(janela, bg=BG_COLOR)
lista_frame.pack(
    pady=scale_size(20, DPI_SCALE),
    padx=scale_size(30, DPI_SCALE),
    fill="both",
    expand=True,
)

# ======================= IMAGEM =======================
# Carregamento da imagem para os contatos
try:
    # Tenta carregar a imagem do arquivo e redimensiona baseado no DPI
    image_size = scale_size(60, DPI_SCALE)
    imagem = Image.open("imagem/person.png").resize(
        (image_size, image_size), Image.Resampling.LANCZOS
    )
except FileNotFoundError:
    # Se não encontrar a imagem, cria uma imagem em branco
    image_size = scale_size(60, DPI_SCALE)
    imagem = Image.new("RGB", (image_size, image_size))

# Converte a imagem para formato compatível com tkinter
img_contato = ImageTk.PhotoImage(imagem)

# ======================= INICIALIZAÇÃO =======================
# Cria cards para todos os contatos na inicialização
for contato in contatos:
    criar_card(contato)

# Inicia o loop principal da interface gráfica
janela.mainloop()
