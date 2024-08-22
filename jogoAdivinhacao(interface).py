import tkinter as tk
from tkinter import messagebox 


import random 


class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        self.root.geometry("300x200") #tamanhdo da janela

        #variaveis do jogo
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

#Adicionaremos alguns widgets como Label, Entry, e Button.

        #interface
        self.label_instrucao = tk.Label(root , text = "Adivinhe um numero, entre 1 0 100!")
        self.label_instrucao.pack()

        self.entrada_palpite = tk.Entry(root)
        self.entrada_palpite.pack()

        self.botao_adivinhar = tk.Button(root, text="Adivinha", command=self.verificar_palpite)
        self.botao_adivinhar.pack()

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def verificar_palpite(self):
            palpite = int(self.entrada_palpite.get())
            self.tentativas +=1

            if palpite < self.numero_secreto:
                self.label_resultado.config(text="Muito beixo! Tente novamente.")
            elif palpite > self.numero_secreto:
                self.label_resultado.config(text="Muito alto! Tente novamente!")
            else:
                self.label_resultado.config(text=f"Parabens! voce adivinhou em {self.tentativas} tentativas.")
                messagebox.showinfo("Vitoria", f"Voce acertou o numero {self.numero_secreto} em {self.tentativas} tentativas!!") 

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.label_resultado.config(text="")
        self.entrada_palpite.delete(0, tk.END)

if __name__ =="__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()




    