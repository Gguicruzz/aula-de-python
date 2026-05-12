import os

# Limpa a tela (Windows). Se não existir, ignora.
try:
    os.system("cls")
except Exception:
    pass



#correção do exercio da ultima aula: try arquivos 

"""
menu 
0-sair 
1-nome 
2-gravar no arquivo 
3-ler o arquivo
escolha: 
"""

while True:  
    print("""
 menu 
 0-sair 
 1-nome 
 2-gravar no arquivo 
 3-ler o arquivo
 escolha: 
 """,end = "")
    opcao = input()

    match opcao: 
        case '0': 
            break
        case '1': 
            nome_arquivo = input("nome do arquivo")
            nome_arquivo = nome_arquivo + ".txt"
            
        case '2':
            
                arq = open(nome_arquivo, "w", encoding="utf-8")
                conteudo = input("Digite um conteúdo: ")
                arq.write(conteudo)
                arq.close()
          
        case '3':
            if 'nome_arquivo' not in locals():
                print("Defina o nome do arquivo primeiro (opção 1).")
                input("Pressione Enter para continuar...")
                continue

            try:
                arq = open(nome_arquivo,"r", encoding="utf-8") # r = read 
                print(f"--------{nome_arquivo}----------")
                print(arq.read())
                arq.close()

            except FileNotFoundError:
                print(f"o arquivo  {nome_arquivo} não encontrado")
            else: # se não houver falha 
                print(f"arquivo {nome_arquivo} exibido com sucesso!")
            finally: 
                print("obrigado por executar!")    
        case '4':
            
            try:
                arq = open(nome_arquivo,"a", encoding="uft-8")
                editar = input("Digite a nova alteração")
                arq.write(f"Nova linha: {editar}" )
                arq.close()
            except FileExistsError: 
                print(f"o arquivo {nome_arquivo} não foi encontrado")   
            else: 
                print(f"alteração feita com sucesso")
            finally: 
                print("obrigado por executar")         

              
             


          




