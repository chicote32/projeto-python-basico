import tkinter as tk
import random 
ale = int(random.random()*100)
chances= 5
limite_maior =100
limite_menor = 0 
def maior ():
    global limite_menor
    global limite_maior
    global ale
    global chances
    if chances <= 0:
        texto.config(text="Acabaram as chances!\nVoçe venceu")
    else:
        limite_menor = ale
        ale = (limite_menor + limite_maior) // 2
        texto.config(text=f"Seu número é {ale}")
        chances = chances-1
        texto2.config(text=f"vidas: {chances}")
    
def menor ():
    global limite_menor
    global limite_maior
    global ale
    global chances
    if chances <= 0:
        texto.config(text="Acabaram as chances!\nVoçe venceu")
    else:
        limite_maior = ale
        ale = (limite_menor + limite_maior) // 2
        texto.config(text=f"Seu número é {ale}")
        chances = chances-1
        texto2.config(text=f"vidas: {chances}")
        
def acertou ():
    if chances < 0:
        texto.config(text="Acabaram as chances!\nVoçe venceu")
    else:
        texto.config(text=f"acertamos seu numero é: {ale}")
def recomeco():
    global limite_menor
    global limite_maior
    global ale
    global chances
    ale = random.randint(0,100)
    chances= 5
    limite_maior =100
    limite_menor = 0 
    texto.config(text=f"Seu número é {ale}") 
    texto2.config(text=f"vidas: {chances}")



janela = tk.Tk()

janela.title("vamos advinhar o seu numero em cinco chances")
janela.geometry("400x300")
texto = tk.Label(janela,text=f"seu numero é {ale}")
texto.pack()
texto2 = tk.Label(janela,text=f"vidas: {chances}")
texto2.pack()
botao = tk.Button(janela,text="maior",command=maior)
botao.pack()
botao2 = tk.Button(janela,text="menor",command=menor)
botao2.pack()
botao3 = tk.Button(janela,text="acertou",command=acertou)
botao3.pack()
botao4 = tk.Button(janela,text="recomeçar",command=recomeco)
botao4.pack()
texto.pack()
janela.mainloop()