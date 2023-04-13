#Declaração de variaveis
fila = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
opcao = 0
inicio = 0 #Onde começa a fila
fim = 0 #Onde termina a fila
total = 0  #O numero de posições ocupadas na fila

#Função de menu, para informar as opções possveis ao usuario
def menu() :
    global opcao
    print("======== MENU ========")
    print("Digite 1 para listar")
    print("Digite 2 para adicionar")
    print("Digite 3 para remover")
    opcao = int(input("Digite a opção "))#variavel que guarda a opção digitada pelo usuario
    print("========= || =========")

#Função para listar a situação da fila
def listar() :
    global fila
    global inicio
    global fim
    global total

    print("===== CONSULTA =====")
    print(fila)
    print("- A fila começa em %d" %inicio)
    print("- A fila termina em %d" %fim)
    print("- A fila tem %d espaços ocupados" %total)
    print("========= || =========")


#Função para adicionar numeros de até 2 digitos na fila
def adicionar() :
    global fim
    global total

    if total == 10 : #Se o numero total de espaços ocupados na fila for 10, ou seja a fila estiver cheia, avise:
        print("======== AVISO =======")
        print("- Fila cheia")
        print("========= || =========")
    else: #Caso contrario, adicione
        print("====== ADICIONAR =====")
        i = int(input("- Digite o numero para adicionar a fila: "))# I guarda o numero que sera adicionado
        if i >= 100 : #Caso o numero seja igual ou maior que 100, ou seja, tiver 3 digitos, avise:
            print("- Numero inválido, por favor insira numeros de até 2 digitos")
            print("========= || =========")
        else : #Se não, adicione a lista, e diga qual numero foi adicionado
            print("- %d adicionado com sucesso" %i)
            print("========= || =========")
        
        #Fazendo a fila girar
        if fim == 10 : #Se a posição final for 10 e houver posições dispoiveis, reinicie o valor para 0
            fim = fim - 10
        else : #Caso contrario adicione a fila e atualize as variaveis e posições ocupadas
            fila[fim] = i 
            fim += 1
            total += 1

#Função para remover algum elemento da fila 
def remover() :
    global inicio
    global fim
    global total

    if total == 0 : #Se o numero de elementos na fila for 0, então ela está vazia
        print("======== AVISO =======")
        print("- Fila vazia")
        print("========= || =========")
    else : #Se tiver elementos dentro da fila, renoma o primeiro
        print("======= REMOÇÃO ======")
        print("- O %d foi removido" % fila[inicio])
        print("========= || =========")

        #Fazendo a fila girar
        if inicio == 10 : #Se o inicio da fila estiver em 10, e este ultimo elemento for removido, o valor de inicio volta a ser 0
            inicio = inicio - 10
        else : #Se não, atualize o valor de incio e abra uma nova vaga, diminuindo o valor de total 
            inicio += 1
            total -= 1
 
#Laço para printar o menu e verificar a opção escolhida
while opcao != -1 :
    menu()
    if opcao == 1 :
        listar() 
    elif opcao == 2 :
        adicionar()
    elif opcao == 3 :
        remover()
    else :
        print("Numero inválido")
    
