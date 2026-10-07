palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar")

for posicao in range(0, len(palavras)):
    tex_atual = palavras[posicao]
    vog_acu = ""
    
    for indice in range(0, len(tex_atual)):
        letra = tex_atual[indice]
        
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vog_acu = vog_acu + letra + " "
            
    print(f"Na palavra {tex_atual.upper()} temos {vog_acu}")   