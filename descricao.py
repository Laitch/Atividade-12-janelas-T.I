import tkinter as tk
from PIL import Image, ImageTk
 
def MostrarDescricao():
    janela = tk.Tk()
    janela.title("Descrição da Startup")
    janela.resizable(True, True)
    janela.geometry("1000x800")
 
    texto_descricao = tk.Label(janela, text="A Big Star é uma startup inovadora que desenvolve soluções tecnológicas para o \n"
"gerenciamento eficiente de instituições educacionais. Nosso principal produto é um \n"
"sistema integrado de gestão escolar que simplifica e automatiza processos \n"
"administrativos, pedagógicos e comunicacionais, facilitando a rotina de gestores, \n"
"professores, alunos e familiares.", font=("Arial", 16))
    
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).pack(pady=(50,0))
 
    texto_descricao.pack(pady=(50,0))
 
    janela.mainloop()  
 
if __name__ == "__main__":
    MostrarDescricao()
 
