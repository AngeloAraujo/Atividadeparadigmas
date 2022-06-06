vetor = []

def inserir():
    global vetor
    lista = []
    vetor = (lista)

    lista.extend(input('Digite o vetor:'))
    print(vetor)


def inserirfor():
    global vetor
    lista = []
    vetor = (lista)

    index = int(input(f'Insira o tamanho do vetor: '))

    for i in range(index):
        lista.extend(input('Digite o valor de cada vetor: '))

    print(vetor)


def remover():
    global vetor
    delete = (input(f'Insira o valor que deseja remover: '))
    vetor.remove(delete)
    print(vetor)


def uniao():
    global vetor
    lista = []
    vetor = (lista)
    vetora = vetor
    index = int(input(f'Insira o tamanho do vetor A: '))

    for i in range(index):
        lista.extend(input('Digite os valores do vetor: '))

    listab = []
    vetor = (listab)
    vetorb = vetor
    index = int(input(f'Insira o tamanho do vetor B: '))

    for i in range(index):
        listab.extend(input('Digite os valores do vetor: '))
    soma = []
    soma = (vetora + vetorb)
    dict_aux = dict.fromkeys (soma)
    resultado = list(dict_aux)
    print(resultado)

def interseccao():
    global vetor
    lista = []
    vetor = (lista)
    vetora = vetor
    index = int(input(f'Insira o tamanho do vetor A: '))

    for i in range(index):
        lista.extend(input('Digite os valores do vetor: '))

    listab = []
    vetor = (listab)
    vetorb = vetor
    index = int(input(f'Insira o tamanho do vetor B: '))

    for i in range(index):
        listab.extend(input('Digite os valores do vetor: '))

    listac = []

    listac = [i for i in vetorb if i in vetora]

    print(listac)

def diferenca():
    global vetor
    lista = []
    vetor = (lista)
    vetora = vetor
    index = int(input(f'Insira o tamanho do vetor A: '))

    for i in range(index):
        lista.extend(input('Digite os valores do vetor: '))

    listab = []
    vetor = (listab)
    vetorb = vetor
    index = int(input(f'Insira o tamanho do vetor B: '))

    for i in range(index):
        listab.extend(input('Digite os valores do vetor: '))

    setvetora= set(vetora)
    setvetorb= set(vetorb)

    diff_set = set(setvetora)^ set(setvetorb)
    print(sorted(diff_set))

def pertencer ():
    global vetor

    proc =  (input(f'Informe o valor para verificar se ele pertence ao conjunto:'))
    if ( proc in vetor):
        print(f'O valor {proc} pertence ao conjunto')
    else:
        print(f'O valor não pertence ao conjunto')

def maior ():
    global vetor

    print(f'Maior valor do vetor é: ',max(vetor))

def menor():
    global vetor
    print(f'Menor valor do vetor é: ', min(vetor))

def iguais ():
    global vetor
    lista = []
    vetor = (lista)
    vetora = vetor
    index = int(input(f'Insira o tamanho do vetor A: '))

    for i in range(index):
        lista.extend(input('Digite os valores do vetor: '))

    listab = []
    vetor = (listab)
    vetorb = vetor
    index = int(input(f'Insira o tamanho do vetor B: '))

    for i in range(index):
        listab.extend(input('Digite os valores do vetor: '))

    setvetora = set(vetora)
    setvetorb = set(vetorb)

    if (set(setvetora)==set(setvetorb)):
        print(f'Os conjuntos são iguais!!')
    else :
        print(f'Os conjuntos não são iguais')

def tamanho():
    global vetor
    print(f'O tamanho do vetor é: ',len(vetor))

def vazio ():
    global  vetor

    if len(vetor) == 0:
        print(f'Esse conjunto é vazio')
    else:
        print(f'Esse conjunto não é vazio')