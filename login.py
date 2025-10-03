import tkinter as tk
from niveldeacesso_alunos import NiveldeAcessoAlunos
from niveldeacesso_funcionarios import NiveldeAcessoFuncionarios
from niveldeacesso_secretaria import NiveldeAcessoSecretaria
import mysql.connector
from PIL import Image, ImageTk
 
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="escola",
    port="3307"
 
)
    
def AbrirJanelaLogin():
    janela = tk.Tk()
    janela.title("Login")
    janela.resizable(True, True)
    janela.geometry("1000x800")
 
    # Widgets
    label_email = tk.Label(janela, text="Email:")
    entrada_email = tk.Entry(janela, width=50)
 
    label_senha = tk.Label(janela, text="Senha:")
    entrada_senha = tk.Entry(janela, width=50, show="*")
 
    label_erro = tk.Label(janela, text="Email ou senha incorretos", font="red")
 
    def clique():
        email = entrada_email.get()
        senha = entrada_senha.get()
 
        if conexao.is_connected():
 
            cursor = conexao.cursor()
 
            #Aluno
            query = "SELECT COUNT(*) FROM aluno WHERE email = %s"
            cursor.execute(query, (email,))  
            resultado_email = cursor.fetchone()
 
            query = "SELECT COUNT(*) FROM aluno WHERE senha = %s"
            cursor.execute(query, (senha,))  
            resultado_senha = cursor.fetchone()
 
            if resultado_email[0] > 0 and resultado_senha[0] > 0:
                print(f"Aluno")
                janela.destroy()
                NiveldeAcessoAlunos()
            else:
                entrada_email.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)
                label_erro.pack()
 
            #Funcionário
            query = "SELECT COUNT(*) FROM trabalhadores WHERE email = %s"
            cursor.execute(query, (email,))  
            resultado_email = cursor.fetchone()
 
            query = "SELECT COUNT(*) FROM trabalhadores WHERE senha = %s"
            cursor.execute(query, (senha,))  
            resultado_senha = cursor.fetchone()
 
            if resultado_email[0] > 0 and resultado_senha[0] > 0:
                print(f"Funcionário")
                janela.destroy()
                NiveldeAcessoFuncionarios()
            else:
                entrada_email.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)
                label_erro.pack()
 
            #Secretária
            query = "SELECT COUNT(*) FROM secretaria WHERE email = %s"
            cursor.execute(query, (email,))  
            resultado_email = cursor.fetchone()
 
            query = "SELECT COUNT(*) FROM secretaria WHERE senha = %s"
            cursor.execute(query, (senha,))  
            resultado_senha = cursor.fetchone()
 
            if resultado_email[0] > 0 and resultado_senha[0] > 0:
                print(f"Funcionário")
                janela.destroy()
                NiveldeAcessoSecretaria()
            else:
                entrada_email.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)
                label_erro.pack()
 
            # Encerrando conexão
            cursor.close()
            conexao.close()
 
    botao_login = tk.Button(janela, text="Login", command=clique, width=20, height=2)
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).pack()
 
    label_email.pack(pady=(70,0))
    entrada_email.pack(pady=(0,10))
    label_senha.pack(pady=(10,0))
    entrada_senha.pack(pady=(0,20))
    botao_login.pack(pady=50)
 
    janela.mainloop()
 
if __name__ == "__main__":
    AbrirJanelaLogin()
 
