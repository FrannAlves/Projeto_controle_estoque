lista_produtos = []


#----------------------------------------COMEÇO DA FUNÇAO CADASTRAR_PRODUTO----------------------------------------

def cadastrar_produto(codigo):#funçao q permite o usuario cadastrar um produto
    print('Bem vindo ao cadastro de Produtos')
    print('O código do produto a ser cadastrado é: {}'.format(codigo))
    nome = input('Digite o nome do produto: ')
    fabricante = input('Digite o nome do fabricante do produto: ')
    valor = float(input('Digite o valor do produto: '))
    dic_produtos = {'codigo'    : codigo,#dicionario onde se encontram os dados cadastrados pelo usuario
                    'nome'      : nome,
                    'fabricante': fabricante,
                    'preço'     : valor}
    lista_produtos.append(dic_produtos.copy())#colocando o dicionari dentro da lista
#----------------------------------------FIM DA FUNÇAO CADASTRAR_PRODUTO-------------------------------------------

#----------------------------------------COMEÇO DA FUNÇAO CONSULTAR_PRODUTO----------------------------------------

def consultar_produto():#funçao para consultar os produtos que foram cadastrados
    while True:
        try:
            print('Bem vindo a CONSULTA de Produtos')
            consultar = int(input('Entre com a opção desejada:\n1- Consultar todos os produtos\n2- Consultar produtos por código\n3- Consultar produtos por fabricante\n4- Retornar\n>>'))
            if consultar == 1:
                print('Opção selecionada: Consultar TODOS os produtos')
                for produto in lista_produtos:#selecionar cada dicionario da minha lista(cada produto da lista_produto)
                    for key, value in produto.items():#SELECIONAR CADA CONJUNTO   CHAVE : VALOR DO DICIONARIO(EX: NOME : PRESUNTO)
                        print('{} : {}'.format(key, value))
            elif consultar == 2:
                print('Opção selecionada: Consultar produtos por CÓDIGO')
                entrada = int(input('Digite o Codigo do produto: '))
                for produto in lista_produtos:
                    if (produto['codigo'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif consultar == 3:
                print('Opção selecionada: Consultar produtos por FABRICANTE')
                entrada = (input('Digite o fabricante do produto: '))
                for produto in lista_produtos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif consultar == 4:
                break
            else:
                print('Opção ivalida .Digite uma das opções mostradas.')
                continue
        except ValueError:
            print('Pare de digitar numeros não inteiros')

#----------------------------------------FIM DA FUNÇAO CONSULTAR_PRODUTO------------------------------------------

#----------------------------------------COMEÇO DA FUNÇAO REMOVER_PRODUTO------------------------------------------

def remover_produto():
    print('Bem vindo ao remover Produto')
    entrada = int(input('Digite o codigo do produto que deseja remover: '))
    for produto in lista_produtos:
        if (produto['codigo'] == entrada):#o produto que tiver o codigo igual ao digitado sera removido da lista
            lista_produtos.remove(produto)

#-------------------------------------------FIM DA FUNÇAO REMOVER_PRODUTO------------------------------------------



#------------------------------------------------COMEÇO DA MAIN------------------------------------------------------
print('Bem vindo ao controle de estoque do Minimercado da Esquina')
codigo_produto = 0

while True:#dentro do laço o menu de opçoes, as condicionais para tratar e o try except que retornará uma msg caso o usuario digite um numero nao inteiro e volta a mostrar o menu de opçoes
    try:
        opcao = int(input('Escolha a opção desejada: \n'
                  '1- Cadastrar Produto\n'
                  '2- Consultar Produto\n'
                  '3- Remover Produto\n'
                  '4- Sair'
                  '\n>>'))
        if opcao == 1:
            codigo_produto+=1
            cadastrar_produto(codigo_produto)
        elif opcao == 2:
            consultar_produto()
        elif opcao == 3:
            remover_produto()
        elif opcao == 4:
            ('Programa encerrado')
            break
        else:
            print('Opção ivalida .Digite uma das opções mostradas.')
            continue
    except ValueError:
        print('Pare de digitar numeros não inteiros')

#---------------------------------------------------FIM DA MAIN------------------------------------------------------
