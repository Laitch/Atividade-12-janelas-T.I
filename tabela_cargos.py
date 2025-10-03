import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
 
def Cargos():
 
    janela = tk.Tk()
    janela.title("Tabela de Cargos")
    janela.geometry("600x400")
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola",
        port=3307
    )
 
    cursor = conexao.cursor()
    cursor.execute("SELECT id_funcao, Validade, Carga_Horaria FROM cargo")
    cargos = cursor.fetchall()
 
    # Cabeçalhos
    headers = ["ID Função", "Validade", "Carga Horária"]
    for col, texto in enumerate(headers):
        tk.Label(janela, text=texto, font="Arial 10 bold", bg="#dfe6e9").grid(row=1, column=col, padx=10, pady=5)
 
    # Dados
    for i, cargo in enumerate(cargos, start=2):
        for j, valor in enumerate(cargo):
            tk.Label(janela, text=str(valor), bg="#f1f2f6").grid(row=i, column=j, padx=10, pady=2)
 
    cursor.close()
    conexao.close()
 
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).grid()
 
    janela.mainloop()
 
if __name__ == "__main__":
    Cargos()
 
 
