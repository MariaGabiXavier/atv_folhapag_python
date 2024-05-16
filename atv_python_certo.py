def Menu():
    print("==========================   MENU   ==========================")
    print("[1] - Inserir funcionários")
    print("[2] - Remover funcionários")
    print("[3] - Determinar a folha de pagamento")
    print("[4] - Determinar relatório com o salário bruto e líquido")
    print("[5] - Imprimir funcionário com maior salário líquido")
    print("[6] - Imprimir funcionário com o maior número de faltas no mês")
    print("[7] - Sair")
    print('='*62)
    Opcao()

def Opcao():
    opc = int(input("Opção: "))

    if opc == 1:
        n = int(input("Quantos funcionários deseja inserir? "))
        cont = 0
        while cont < n:
            cont += 1
            InserirFunc()
        Menu()
    elif opc == 2:
        n = int(input("Quantos funcionários deseja remover? "))
        cont = 0
        while cont < n:
            cont += 1
            RemoverFunc()
        Menu()
    elif opc == 3:
        FolhaPgto()
    elif opc == 4:        
        Relatorio()
    elif opc == 5:
        FuncMaiorSL()
    elif opc == 6:
        FuncMaiorNF()
    elif opc == 7:
       print("Programa finalizado.")
    else:
        print("Número inválido!")
        Menu()

def InserirFunc():
    print("--- Inserir funcionários ---")
    mat = int(input("Matrícula: "))
    nome = input("Nome: ")
    cod = int(input("Código da função [101 - Vendedor | 102 - Administrativo]: "))
    if cod == 101:
        salfixo = 1500.00
    elif cod == 102:
        salfixo = float(input("Salário fixo: "))
    else:
        print("Código Inválido! Digite novamente...")
        return
    faltas = int(input("Número de faltas: "))
    salbruto = SalBruto(cod, faltas, salfixo)
    percimp = Perc(salfixo)
    ip = Imp(salfixo)
    desc = Desc(salfixo, faltas)
    salliquido = SalLiquido(salfixo, salbruto)
    inf.append(nome)
    inf.append(cod)
    inf.append(faltas)
    inf.append(salbruto)
    inf.append(percimp)
    inf.append(ip)
    inf.append(desc)
    inf.append(salliquido)
    func[mat] = [nome, cod, faltas, salbruto, percimp, ip, desc, salliquido]
    funcionario.update(func)
    print('-'*62)

def SalBruto(cod, faltas, salfixo):
    if cod == 101:
        porc = salfixo * 0.09
        descflt = Desc(salfixo, faltas)
        salbrt = salfixo + porc - descflt
    elif cod == 102:
        descflt = Desc(salfixo, faltas)
        salbrt = salfixo - descflt
    print(f"Salário bruto: {salbrt:.2f}")
    return salbrt

def SalLiquido(salfixo, salbruto):
    if salfixo <= 2259.20:
        sallqd = salbruto
    elif salfixo <= 2828.65:
        sallqd = salfixo - Imp(salfixo)
    elif salfixo <= 3751.05:
        sallqd = salfixo - Imp(salfixo)
    elif salfixo <= 4664.68:
        sallqd = salfixo - Imp(salfixo)
    else:
        sallqd = salfixo - Imp(salfixo)
    print(f"Salário líquido: {sallqd:.2f}")
    return sallqd

def Perc(salfixo):
    if salfixo <= 2259.20:
        perc = "Isento"
    elif salfixo <= 2828.65:
        perc = "7,5%"
    elif salfixo <= 3751.05:
        perc = "15%"
    elif salfixo <= 4664.68:
        perc = "22,5%"
    else:
        perc = "27,5%"
    print(f"Percentual do Imposto: {perc}")
    return perc

def Imp(salfixo):
    if salfixo <= 2259.20:
        imp = 0
    elif salfixo <= 2828.65:
        imp = salfixo * 0.075
    elif salfixo <= 3751.05:
        imp = salfixo * 0.15
    elif salfixo <= 4664.68:
        imp = salfixo * 0.225
    else:
        imp = salfixo * 0.275
    return imp

def Desc(salfixo, faltas):
    if salfixo <= 2259.20:
        desc = faltas * (salfixo/30)
    elif salfixo <= 2828.65:
        desc = faltas * (salfixo/30)
    elif salfixo <= 3751.05:
        desc = faltas * (salfixo/30)
    elif salfixo <= 4664.68:
        desc = faltas * (salfixo/30)
    else:
        desc = faltas * (salfixo/30)
    return desc

def RemoverFunc():
    print("--- Remover funcionários ---")
    r = int(input("Número de matrícula do Funcionário a ser removido: "))
    c = input(f"Deseja remover o funcionário {funcionario[r]} [S/N]? ").upper()
    if c == 'S':
        if r in funcionario:
            del funcionario[r]
            print("Funcionário removido.")
        else:
            print("Funcionário não encontrado")
            return RemoverFunc()
    else:
        print("Certo, retornando...\n")
        return RemoverFunc()
    print('-'*62)

def FolhaPgto():
    n = int(input("Deseja determinar a folha de pagamento de qual funcionário (digite a matrícula)? "))
    print("--- Folha de Pagamento ---")
    if n in funcionario:
        for mat, inf in func.items():
            if n == mat:
                print(f"Matrícula: {mat}")
                print(f"Nome: {inf[0]}")
                print(f"Código: {inf[1]}")
                print(f"Faltas: {inf[2]}")
                print(f"Salário bruto: {inf[3]:.2f}")
                print(f"Percentual de Imposto: {inf[4]}")
                print(f"Valor do Imposto: {inf[5]:.2f}")
                print(f"Salário líquido: {inf[7]:.2f}")
    else:
        print("Funcionário não encontrado.")   
        FolhaPgto()
    Menu()

def Relatorio():
    print(funcionario)
    print("--- Relatório ---")
    for mat, inf in funcionario.items():
        print(f"Matrícula: {mat}")
        print(f"Nome: {inf[0]}")
        print(f"Código: {inf[1]}")
        print(f"Salário bruto: {inf[3]:.2f}")
        print(f"Salário líquido: {inf[7]:.2f}")
        print("-"*40)
    Menu()

def FuncMaiorSL():
    maiorsl = 0
    for maior in funcionario.values():
        lqd = maior[7]
        if lqd > maiorsl:
            maiorsl = lqd
    for mat, inf in func.items():
        if inf[7] == maiorsl:
            print(f"Matrícula: {mat}")
            print(f"Nome: {inf[0]}")
            print(f"Código: {inf[1]}")
            print(f"Salário bruto: {inf[3]:.2f}")
            print(f"Percentual de Imposto: {inf[4]}")
            print(f"Salário líquido: {inf[7]:.2f}")
    Menu()  

def FuncMaiorNF():
    maiorflt = 0
    for maior in funcionario.values():
        faltas = maior[2]
        if faltas > maiorflt:
            maiorflt = faltas
    for mat, inf in func.items():
        if inf[2] == maiorflt:
                print(f"Matrícula: {mat}")
                print(f"Nome: {inf[0]}")
                print(f"Código: {inf[1]}")
                print(f"Faltas: {inf[2]}")
                print(f"Desconto no salário: {inf[2]:.2f}")
    Menu()

funcionario = {}
func = {}
inf = []

Menu()