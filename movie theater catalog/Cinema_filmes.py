import os

class Filme:
    deletado = 0
    titulo = "desconhecido"
    genero = "desconhecida"
    duracao = -1
    ano = -1
    codigo = -1

def abrir_arquivo_filme(nome_arquivo):
    filmes = []
    if not os.path.exists("filmes.txt"):
        return filmes
    arq = open(f"{nome_arquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        filme = Filme()
        filme.deletado = int(infos[0])
        filme.titulo = infos[1]
        filme.genero = infos[2]
        filme.duracao = int(infos[3])
        filme.ano = int(infos[4])
        filme.codigo = int(infos[5])
        filmes.append(filme)
    arq.close()
    return filmes

def salvar_filmes(filmes):
    arq = open("filmes.txt",'w')
    for filme in filmes:
        arq.write(str(filme.deletado) + ';' + filme.titulo + ';' + filme.genero + ';' + str(filme.duracao) + ';' + str(filme.ano) + ';' + str(filme.codigo) + "\n")
    arq.close

def codigo_existente(lista_filmes,code):
    for elem in lista_filmes:
        if code == elem.codigo and elem.deletado == 0:
            print("Código inválido!!!")
            print()
            return True
    return False   

def Inserindo_filme(lista_filmes):
    filme = Filme()
    filme.deletado = 0
    filme.titulo = input("Digite o título: ")
    filme.genero = input("Digite o genero do filme: ")
    filme.duracao = int(input("Digite a duração do filme: "))
    filme.ano = int(input("Digite o ano de lançamento do filme: "))
    filme.codigo = int(input("Digite o código do filme: "))
    achou = True
    while achou:
        achou = codigo_existente(lista_filmes,filme.codigo)
        if achou:
            filme.codigo = int(input("Digite outro código para o Filme: "))
    lista_filmes.append(filme)
    print("Filme adicionado com sucesso!")

def listando_filme(lista_filmes):
    if len(lista_filmes) <= 0:
        print("Não há filmes no catálogo.")
    else:
        numero_filmes = 0
        indice_filme = 0
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        for filme in lista_filmes:
            if filme.deletado == 0:
                numero_filmes += 1
                print(f"Filme [{numero_filmes}]:")
                imprime_filme(lista_filmes,indice_filme)
                print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
            indice_filme += 1

def imprime_filme(lista_filmes,indice):
    print(f"Título: {lista_filmes[indice].titulo}")
    print(f"Gênero: {lista_filmes[indice].genero}")
    print(f"Duração: {lista_filmes[indice].duracao} min")
    print(f"Ano de lançamento: {lista_filmes[indice].ano}")
    print(f"Código: {lista_filmes[indice].codigo}")

def procurando_filme(lista_filme):
    code = int(input("Digite o código do filme: "))
    achou = False
    i = 0
    print()
    for filme in lista_filme:
        if filme.codigo == code and filme.deletado == False:
            achou = True
            print("Filme encontrado!!")
            print("-=-=-=-=-=--=-=-=-=-=-=-=-")
            imprime_filme(lista_filme,i)
            print("-=-=-=-=-=--=-=-=-=-=-=-=-")
            break
        i += 1
    if achou == False:
        print("Não há nenhum filme com este código.")

def remover_filme(lista_filmes):
    code = int(input("Insira o código do filme: "))
    deletou = False
    for filme in lista_filmes:
        if code == filme.codigo and filme.deletado == 0:
            filme.deletado = 1
            deletou = True
            print("Deletado com sucesso!")
            break
    if not deletou:
        print("O Filme não foi encontrado.")
    return lista_filmes

def editar_filme(lista_filmes):
    code = int(input("Digite o código do filme que deseja editar: "))
    indice = buscar_filme(lista_filmes,code)
    if indice >= 0:
        opcao = menu_editar_filme()
        if opcao == '1':
            print("Alterando título do filme:")
            print()
            return editar_titulo_filme(lista_filmes,indice)
        elif opcao == '2':
            print("Alterando gênero do filme:")
            print()
            return editar_genero_filme(lista_filmes,indice)
        elif opcao == '3':
            print("Alterando duração do filme:")
            print()
            return editar_duracao_filme(lista_filmes,indice)
        elif opcao == '4':
            print("Alterando Ano de Lançamento do filme:")
            print()
            return editar_ano_filme(lista_filmes,indice)
        elif opcao == '5':
            print("Altrerando Código do filme:")
            print()
            return editar_codigo_filme(lista_filmes,indice)
        elif opcao == '0':
            print("Voltando...")
            return lista_filmes
        print("Opção não reconhecida!")
    return lista_filmes

def menu_editar_filme():
    print("O que deseja editar?")
    print()
    print("Titulo..............[1]")
    print("Gênero..............[2]")
    print("Duração.............[3]")
    print("Ano de lançamento...[4]")
    print("Código..............[5]")
    print("Voltar..............[0]")
    opcao = input("-------------------->")
    return opcao

def buscar_filme(lista_filmes,codigo):
    i = 0
    for filme in lista_filmes:
        if codigo == filme.codigo and filme.deletado == 0:
            return i
        i += 1
    print("Filme não encontrado")
    return -1

def editar_titulo_filme(lista_filmes,indice):
    print(f"Título atual: {lista_filmes[indice].titulo}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    lista_filmes[indice].titulo = input("Título novo: ")
    return lista_filmes

def editar_genero_filme(lista_filmes,indice):
    print(f"Gênero atual: {lista_filmes[indice].genero}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    lista_filmes[indice].genero = input("Gênero novo: ")
    return lista_filmes

def editar_duracao_filme(lista_filmes,indice):
    print(f"Duração atual: {lista_filmes[indice].genero}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    lista_filmes[indice].duracao = int(input("Duração nova: "))
    return lista_filmes

def editar_ano_filme(lista_filmes,indice):
    print(f"Ano de Lançamento atual: {lista_filmes[indice].ano}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    lista_filmes[indice].ano = int(input("Ano de Lançamento novo: "))
    return lista_filmes

def editar_codigo_filme(lista_filmes,indice):
    print(f"Código atual: {lista_filmes[indice].codigo}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    code = int(input("Código novo: "))
    achou = True
    while achou:
        achou = codigo_existente(lista_filmes,code)
        if achou:
            code = int(input("Digite outro código para o Filme: "))
    lista_filmes[indice].codigo = code
    print("Código mudado com sucesso!!")
    return lista_filmes