import tkinter as tk
from login import AbrirJanelaLogin
from descricao import MostrarDescricao
import webbrowser as web
 
janela = tk.Tk()
janela.title("Bem vindo!")
janela.resizable = True
janela.geometry("1000x800")
 
label_nome = tk.Label(janela, text="Big Star", font=("Arial", 24))
label_slogan = tk.Label(janela, text="Mudando o ensino e a gestão escolar!", font=("Arial", 12, "bold", "italic"))
imagem = tk.PhotoImage(file="C:\\Users\\MOBSP-041\\Downloads\\Design sem nome (1).png")
label_imagem = tk.Label(janela, image=imagem)
 
def clique_saiba_mais():
    janela.destroy()
    MostrarDescricao()
 
def clique_acessar():
    janela.destroy()
    AbrirJanelaLogin()
 
def clique_localizacao():
    web.open("https://www.google.com/maps/place/Senac+Na%C3%A7%C3%B5es+Unidas/@-23.6698282,-46.7017363,17z/data=!3m1!4b1!4m6!3m5!1s0x94ce515bb231b5ed:0x327b78892baef8e6!8m2!3d-23.6698282!4d-46.6991614!16s%2Fg%2F11hz9r7dzb?entry=ttu&g_ep=EgoyMDI1MDkxNy4wIKXMDSoASAFQAw%3D%3D")
 
botao_acessar = tk.Button(janela, text="Acessar", command=clique_acessar, width=30, height=2)
botao_saibamais = tk.Button(janela, text="Saiba mais", height=1, command=clique_saiba_mais)
botao_localizacao = tk.Button(janela, text="Localização", height=1, command=clique_localizacao)
 
botao_saibamais.pack(anchor="nw")
botao_localizacao.pack(anchor="nw", pady=(30,0))
label_nome.pack(pady=(10,0))
label_slogan.pack()
botao_acessar.pack(pady=(50,0))
label_imagem.pack(pady=(50,0))
janela.mainloop()
 
