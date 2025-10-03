import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import io
 
def Funcionario():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola",
        port=3307
    )
 
    janela = tk.Tk()
    janela.title("Tabela de Funcionários")
    janela.geometry("1200x800")
 
    cursor = conexao.cursor()
    cursor.execute("SELECT id_Funcionario, Nome, email, senha, Foto, Turno FROM trabalhadores")
    funcionarios = cursor.fetchall()
 
    headers = ["ID", "Nome", "Email", "Senha", "Foto", "Turno"]
    for col, texto in enumerate(headers):
        tk.Label(janela, text=texto, font="Arial 10 bold", bg="#dfe6e9").grid(row=1, column=col, padx=10, pady=5)
 
    imagens = []  
 
    for i, funcionario in enumerate(funcionarios, start=2):
        for j, valor in enumerate(funcionario):
            if j == 4 and valor: 
                imagem_binaria = io.BytesIO(valor)
                imagem = Image.open(imagem_binaria)
                imagem = imagem.resize((200, 200))
                imagem_tk = ImageTk.PhotoImage(imagem)
                imagens.append(imagem_tk)
                tk.Label(janela, image=imagem_tk).grid(row=i, column=j, padx=10, pady=2)
            else:
                tk.Label(janela, text=str(valor), bg="#f1f2f6").grid(row=i, column=j, padx=10, pady=2)
 
    cursor.close()
    conexao.close()
    janela.mainloop()
 
if __name__ == "__main__":
    Funcionario()
 
