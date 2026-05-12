with open("arq02.txt","w+", encoding="utf-8") as arq:
    arq.write("nova linha1")
    arq.write("nova linha2")
    arq.write("nova linha3")
    arq.write("nova linha4")
    arq.seek(0) # posiciona o cursor no inicio do arquivo 
    print(arq.read())
    arq.seek(8)
    print(arq.readline())
    print(0)
    linhas_arq = arq.readlines()
    print(linhas_arq[1])