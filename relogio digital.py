import tkinter as tk
import time

def atualizar_tempo():
    hora_atual = time.strftime("%H:%M:%S")
    texto.config(text=hora_atual)
    janela.after(1000, atualizar_tempo)

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("250x100")
janela.configure(bg="black")

texto = tk.Label(janela, font=("courier", 40), bg="black", fg="lime")
texto.pack(anchor="center")

atualizar_tempo()
janela.mainloop()
