import tkinter as tk
import socket
import webbrowser
import random
import requests

def abrir_canal():
    url = 'https://www.youtube.com/@AuthenticGames'
    url2 = 'https://www.youtube.com/@cursoemvideo'
    url3 = random.randint(1, 2)
    if url3 == 1:
        webbrowser.open(url)
    elif url3 == 2:
        webbrowser.open(url2)
ip_publico = requests.get('https://api.ipify.org').text 
janela = tk.Tk()
janela.title(f'Clique no Quadrado, VOCE FOI HACKEADO CARAI kk {ip_publico}')
janela.geometry('300x300')

quadrado = tk.Frame(janela, width=150, height=150, bg="red", cursor="hand2")
quadrado.pack(pady=50)

quadrado.bind("<Button-1>", lambda e: abrir_canal())

label = tk.Label(quadrado, text=f"Clique Aqui {ip_publico}", bg="blue", fg="white", font=("Arial", 12, "bold"))
label.place(relx=0.5, rely=0.5, anchor="center")

janela.mainloop()