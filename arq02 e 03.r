import os 
os.system("cls")

arq = open("arq01.txt", "a", enconding="utf-8") # a = append (acreseentar)
arq.write("nova linha")
arq.close()

# exercio 
# Ao digitar o nome do arquivo, acrescente o .txt automaticamente 
# criar a opcao 4 com edicao de arquivo  


with open("arq02.txt","w+", encoding="utf-8") as arq:
    arq.write("nova linha")
    arq.seek(0) # posiciona o cursor no inicio do arquivo 
    print(arq.read())
