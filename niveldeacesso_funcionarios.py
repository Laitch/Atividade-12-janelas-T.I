import tkinter as tk
import mysql.connector
from tabela_produtos import Produtos
from tabela_alunos import Alunos
 
def NiveldeAcessoFuncionarios():
 conexao = mysql.connector.connect(
 host="localhost",
 user="root",
 password="", 
 database="escola",
 port="3307"
 
)
 cursor = conexao.cursor()
 
 query = "SELECT Direitos FROM nivel_de_acesso WHERE ChaveDeAcesso = %s"
 cursor.execute(query, (2,))
 
 resultado = cursor.fetchone()
 
 cursor.close()
 conexao.close()
 
 janela = tk.Tk()
 janela.title("Nível de Acesso")
 janela.resizable = True
 janela.geometry("1000x800")
 
 def clique_produtos():
 janela.destroy()
 Produtos()
 
 def clique_alunos():
 janela.destroy()
 Alunos()
 
 label_nome = tk.Label(janela, text="Nível de Acesso: Funcionário", font=("Arial", 24))
 imagem = tk.PhotoImage(file="C:\\Users\\MOBSP-041\\Downloads\\Design sem nome (1).png")
 label_imagem = tk.Label(janela, image=imagem)
 label_descricao = tk.Label(janela, text=resultado, font=("Arial", 18))
 botao_acessar_alunos = tk.Button(janela, text="Acessar tabela de alunos", command=clique_alunos, height=3, width=40)
 botao_acessar_produtos = tk.Button(janela, text="Acessar Produtos", command=clique_produtos, height=3, width=40)
 
 label_nome.pack(pady=(100,0))
 label_descricao.pack()
 label_imagem.pack(pady=(50,0))
 botao_acessar_alunos.pack(pady=(40,0))
 botao_acessar_produtos.pack(pady=(10,0))
 janela.mainloop()
 
if __name__ == "__main__":
 NiveldeAcessoFuncionarios()
 
 
