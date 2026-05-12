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

# Exercio, grave ao menos 4 linhas em um arquivo 
# peça para o usuario escolher uma linha 
# - exiba na tela a linha 
# - conte quantas palavras há na linha 
# - conte quantos caracteres há na linha      

with open("arq03.txt","w+", encoding="uft-8") as arq: 
    
    arq.write("Nova linha")
    arq.write("Nova linha")
    arq.write("Nova linha")
    arq.write("Nova linha")
    arq.seek(0)
    escolha = input("escolha uma linha: ")
    linha = arq.readline(escolha)
    print(arq.readline())
    len(linha)
    linha.count()

