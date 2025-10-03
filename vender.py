import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
 
def Vender():
 
    def inserir_venda():
        id_produto = entry_produto.get()
        id_comprador = entry_funcionario.get()
 
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escola",
            port=3307
        )
 
        cursor = conexao.cursor()
 
        query = "INSERT INTO vendas (Id_Produtos, Id_Comprador) VALUES (%s, %s)"
        valores = (id_produto, id_comprador)
        nome = "SELECT nome FROM produtos WHERE id_Produtos = %s"
        cursor.execute(nome, (id_produto,))
        resultado = cursor.fetchone()
 
        try:
            cursor.execute(query, valores)
            conexao.commit()
            resultado_label.config(text=f"Venda de {resultado} registrada com sucesso!", fg="green")
        except Exception as e:
            resultado_label.config(text=f"Insira os valores corretos", fg="red")
 
        cursor.close()
        conexao.close()
 
    # Interface gráfica
    janela = tk.Tk()
    janela.title("Comprar")
    janela.geometry("400x300")
 
    imagem = Image.open("C:\\Users\\MOBSP-041\\Downloads\\Imagem-do-WhatsApp-de-2025-10-02-à_s_-12.41.03_57ac9cfe.png")
 
    # Redimensiona a imagem
    imagem_diminuida = imagem.resize((200, 200))
 
    # Converte para usar no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_diminuida)
 
    label_imagem = tk.Label(janela, image=imagem_tk).pack()
 
    # Labels e campos
    tk.Label(janela, text="ID do Produto:", font="Arial 12").pack(pady=10)
    entry_produto = tk.Entry(janela, font="Arial 12")
    entry_produto.pack()
 
    tk.Label(janela, text="ID do Comprador:", font="Arial 12").pack(pady=10)
    entry_funcionario = tk.Entry(janela, font="Arial 12")
    entry_funcionario.pack()
 
    # Botão de envio
    tk.Button(janela, text="Comprar", command=inserir_venda, font="Arial 12 bold").pack(pady=20)
 
    # Resultado
    resultado_label = tk.Label(janela, text="", font="Arial 10")
    resultado_label.pack()
 
    janela.mainloop()
 
 
if __name__ == "__main__":
    Vender()
 
