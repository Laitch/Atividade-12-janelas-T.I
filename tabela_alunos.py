import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import io
 
def Alunos():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola",
        port=3307
    )
 
    janela = tk.Tk()
    janela.title("Tabela de Alunos")
    janela.geometry("1200x800")
 
    cursor = conexao.cursor()
    cursor.execute("SELECT id_aluno, nome, sala, registro, email, senha, foto FROM aluno")
    alunos = cursor.fetchall()
 
    headers = ["ID", "Nome", "Sala", "Registro", "Email", "Senha", "Foto"]
    for col, texto in enumerate(headers):
        tk.Label(janela, text=texto, font="Arial 10 bold", bg="#dfe6e9").grid(row=1, column=col, padx=10, pady=5)
 
    imagens = []  # manter referência das imagens para não serem coletadas
 
    for i, aluno in enumerate(alunos, start=2):
        for j, valor in enumerate(aluno):
            if j == 6 and valor:  # coluna da foto
                imagem_binaria = io.BytesIO(valor)
                imagem = Image.open(imagem_binaria)
                imagem = imagem.resize((200, 250))
                imagem_tk = ImageTk.PhotoImage(imagem)
                imagens.append(imagem_tk)  # evitar coleta de lixo
                tk.Label(janela, image=imagem_tk).grid(row=i, column=j, padx=10, pady=2)
            else:
                tk.Label(janela, text=str(valor), bg="#f1f2f6").grid(row=i, column=j, padx=10, pady=2)
 
    cursor.close()
    conexao.close()
    janela.mainloop()
 
if __name__ == "__main__":
    Alunos()
 
