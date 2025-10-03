import tkinter as tk
from tabela_produtos import Produtos
from tabela_alunos import Alunos
from tabela_cargos import Cargos
from tabela_trabalhador import Funcionario
from tabela_secretaria import Secretaria
from PIL import Image, ImageTk
 
def NiveldeAcessoSecretaria():
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
 
    def clique_cargos():
        janela.destroy()
        Cargos()
    
    def clique_funcionarios():
        janela.destroy()
        Funcionario()
    
    def clique_secretaria():
        janela.destroy()
        Secretaria()
 
    label_nome = tk.Label(janela, text="Nível de Acesso: Secretaria", font=("Arial", 24))
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).pack()
    botao_acessar_alunos = tk.Button(janela, text="Acessar Tabela de Alunos", command=clique_alunos, height=3, width=40)
    botao_acessar_produtos = tk.Button(janela, text="Acessar Produtos", command=clique_produtos, height=3, width=40)
    botao_acessar_cargo = tk.Button(janela, text="Acessar Tabela de Cargos", command=clique_cargos, height=3, width=40)
    botao_acessar_funcionarios = tk.Button(janela, text="Acessar Tabela de Funcionários", command=clique_funcionarios, height=3, width=40)
    botao_acessar_secretaria = tk.Button(janela, text="Acessar Tabela da Secretária", command=clique_secretaria, height=3, width=40)
 
    label_nome.pack()
    botao_acessar_alunos.pack(pady=(20,0))
    botao_acessar_produtos.pack(pady=(10,0))
    botao_acessar_cargo.pack(pady=(10,0))
    botao_acessar_funcionarios.pack(pady=(10,0))
    botao_acessar_secretaria.pack(pady=(10,0))
    janela.mainloop()
 
if __name__ == "__main__":
    NiveldeAcessoSecretaria()
 
