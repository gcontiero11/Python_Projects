from Cinema_filmes import *

class Filme:
    deletado = 0
    titulo = "desconhecido"
    genero = "desconhecida"
    duracao = -1
    ano = -1
    codigo = -1

def menu():
    print("Filmes")
    print("      Inserir filme....[1]")
    print("      Listar filmes....[2]")
    print("      Procurar filme...[3]")
    print("      Remover filme....[4]")
    print("      Editar filme.....[5]")
    print("Salas")
    print("      Inserir Sala.....[6]")
    print("      Listar Salas.....[7]")
    print("Sair...................[0]")
    opcao = input("----------------------> ")
    print()
    return opcao   

def main():
    filmes = abrir_arquivo_filme("filmes.txt")
    opcao = "x"
    while opcao != '0':
        opcao = menu()
        if opcao == '1':
            print("Inserindo filme...")
            print()
            Inserindo_filme(filmes)
            salvar_filmes(filmes)
            print()
        elif opcao == '2':
            print("Listando Filme...")
            print()
            listando_filme(filmes)
            print()
        elif opcao == '3':
            print("Procurando filme...")
            print()
            procurando_filme(filmes)
            print()
        elif opcao == '4':
            print("Removendo Filme...")
            filmes = remover_filme(filmes)
            print()
        elif opcao == '5':
            print("Editando filme...")
            print()
            filmes = editar_filme(filmes)
            print()
        elif opcao == '0':
            print("Saindo do Programa...")
            salvar_filmes(filmes)
        else:
            print("Opção invalida!!!")
            print()

main()
