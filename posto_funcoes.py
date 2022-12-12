def caixa_de_texto(string):
    print("\n", "-" * 50, "\n", " " * ((50-len(string))//2), string, "\n", "-" * 50, '\n')

def exibir_opcoes(opcoes):

    caixa_de_texto('O melhor Posto do mundo')
    
    for i in range(len(opcoes)):

        print(f'{i+1} - {opcoes[i]}')


def mostra_combustivel(nome_lista, lista, caractere):

    caixa_de_texto(nome_lista)

    if not(len(lista) == 0):
        
            for x in lista:

                print(f'{caractere}- {x.getNome()}' + ' ' * (10 - len(x.getNome())) + f'|  R$ {round(x.getPreco(), 2):.2f}' + f'  |  {round(x.getEstoque(), 2):.2f} Litros em estoque')
                
                if (type(caractere) == int):

                    caractere += 1
                
    else:
        print('\nLista vazia')


def mostra_veiculos(lista) :

    for i in range(len(lista)):

        print(f'{i+1}- {lista[i]}')


def mostra_extrato(nome_lista, lista):
    faturamento = 0

    caixa_de_texto(nome_lista)
    print()

    for x in lista:
        if x.getPreco() < 0:
            print(' -  R$ {:.2f}'.format(x.getPreco()*-1) + ' ' * (10 - len(str(x.getPreco()))) +  '|   {:.2f} litros de {} adquiridos'.format(x.getQuantidade(), x.getTipo()))
            faturamento = faturamento + x.getPreco()

        if x.getPreco() > 0:
            print(' +  R$ {:.2f}'.format(x.getPreco()) + ' ' * (10 - len(str(x.getPreco()))) +  '|   {:.2f} litros de {} abastecidos em "{}"'.format(x.getQuantidade(), x.getTipo(), x.getVeiculo()))
            faturamento = faturamento + x.getPreco()

    print()
    caixa_de_texto('Dinheiro total: R$ {:.2f}'.format(round(faturamento, 2)))

def Input(tipo, texto, limite, minLimite, maxLimite, cancelavel, completar, completarValor):
    inpuT = input('\n {}'.format(texto))
    while not(type(inpuT) == tipo):
        try:
            if cancelavel == 1:
                if inpuT.capitalize() == 'X':
                    break

            if completar == 1:
                if inpuT == "Completar":
                    inpuT = completarValor
                    break

            inpuT = tipo(inpuT)

            if limite == 3:
                if not inpuT >= 0:
                    raise ValueError
                round(inpuT, 2)
                break

            if limite == 2:
                if not minLimite <= inpuT <= maxLimite:
                    raise ValueError
                round(inpuT, 2)
                break

            if limite == 1:
                if not inpuT > 0:
                    raise ValueError
                round(inpuT, 2)
                break

            if limite == 0:
                round(inpuT, 2)
                break
        except:
            print('\n Valor digitado inválido, por favor digite novamente')
            inpuT = input('\n {}'.format(texto))

    return inpuT


