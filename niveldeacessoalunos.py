import tkinter as tk
import mysql.connector
from tabela_produtos import Produtos
from PIL import Image, ImageTk
 
def NiveldeAcessoAlunos():
 
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="escola",
    port="3307"
 
)
    janela = tk.Tk()
    janela.title("Nível de Acesso")
    janela.resizable = True
    janela.geometry("1000x800")
 
    cursor = conexao.cursor()
 
    query = "SELECT Direitos FROM nivel_de_acesso WHERE ChaveDeAcesso = %s"
    cursor.execute(query, (3,))
 
    resultado = cursor.fetchone()
 
    cursor.close()
    conexao.close()
 
    label_nome = tk.Label(janela, text="Nível de Acesso: Aluno", font=("Arial", 24))
    label_descricao = tk.Label(janela, text=resultado, font=("Arial", 18))
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).pack()
 
    def clique_produtos():
        janela.destroy()
        Produtos()
 
    botao_acessar_produtos = tk.Button(janela, text="Acessar Produtos", command=clique_produtos, height=3, width=40)
 
    label_nome.pack(pady=(100,0))
    label_descricao.pack()
    botao_acessar_produtos.pack(pady=(40,0))
    janela.mainloop()
 
if __name__ == "__main__":
    NiveldeAcessoAlunos()
 
