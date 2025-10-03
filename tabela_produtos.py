import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from vender import Vender
 
def Produtos():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="escola",
        port=3307
    )
 
    janela = tk.Tk()
    janela.title("Produtos")
    janela.geometry("1000x800")
    
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk)
    label_imagem.grid(row=0, column=0, columnspan=5, sticky="nw", padx=10, pady=10)
 
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
 
    # Cabeçalhos
    headers = ["ID", "Nome", "Preço", "Quantidade"]
    for col, texto in enumerate(headers):
        tk.Label(janela, text=texto, font="Arial 10 bold").grid(row=1, column=col, padx=10, pady=5)
 
    # Dados
    for i, produto in enumerate(produtos, start=2):
        for j, valor in enumerate(produto):
            tk.Label(janela, text=str(valor)).grid(row=i, column=j, padx=10, pady=2)
 
    cursor.close()
    conexao.close()
 
    def clique_comprar():
        janela.destroy()
        Vender()
 
    botao_comprar = tk.Button(janela, text="Comprar", command=clique_comprar, height=3, width=40)
 
    botao_comprar.grid(row=6, column=3)
    janela.mainloop()
 
if __name__ == "__main__":
    Produtos()
 
