import csv
acidentes = []
def carrega_arquivo():
    with open('acidentes.csv', mode='r', encoding="utf-8")as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            acidentes.append(linha)

def titulo(text, sublinhado = "-"):
    print()
    print(text)
    print(sublinhado*40)

def acidentes_ano():
    titulo('Dados de acidentes por ano')

    num = len(acidentes)
    num_2021 = 0
    num_2022 = 0
    num_2023 = 0

    for acidente in acidentes:
        if"2021" in acidente["CRASH DATE"]:
            num_2021 += 1
        elif"2022" in acidente["CRASH DATE"]:
            num_2022 += 1
        elif "2023" in acidente["CRASH DATE"]:
            num_2023 += 1
        
    print(f"\n Nº total de acidentes: {num:_.0f}".replace('_',"."))
    print(f"\nNº de acidentes em 2021: {(num-num_2021-num_2022-num_2023):_.0f}".replace("_","."))
    print(f"Nº de acidentes em 2021: {num_2021:_.0f}".replace('_',"."))
    print(f"Nº de acidentes em 2022: {num_2022:_.0f}".replace('_',"."))
    print(f"Nº de acidentes em 2023: {num_2023:_.0f}".replace('_',"."))
   

def acidentes_bairro():
    titulo('Dados de acidentes por bairro')

    dicionario = {}

    for acidente in acidentes:
        num = dicionario.get(acidente["BOROUGH"], None)
        if num == None:
            dicionario[acidente['BOROUGH']] = 1
        else:
            dicionario[acidente['BOROUGH']] = num +1
    lista = sorted(dicionario.items(), key=lambda dic: dic[1], reverse=True)

    print("\nBairro..............: N° Acidentes")

    for (bairro, num ) in lista:
        if bairro == "":
            print(f"{'Não informada':20} {num}")

        else:
            print(f"{bairro:20} {num}")
def filtro_por_automovel ():
    titulo('Dados de acidentes por automovel')
    print("-" * 30)

    def bike():
        bike = 0
        for acidente in acidentes:
            for i in range(1 , 6):
                if "BIKE" in acidente[f"VEHICLE TYPE CODE {i}"].upper():
                    bike += 1
        print()
        print("resultado")
        print(f'\nNº bikes: {bike}')
        print()
    def buss():
        bus=0
        for acidente in acidentes:
            for i in range(1,6):
                if "BUS" in acidente[f"VEHICLE TYPE CODE {i}"].upper():
                    bus += 1
        print()
        print("\nresultado")
        print(f"Nº bus: {bus}")
        print()

    def Sedan():
        sedan =0
        for acidente in acidentes:
             for i in range(1,6):
                 if "SEDAN"in acidente[f"VEHICLE TYPE CODE {i}"].upper():
                     sedan += 1
        print()
        print("\nresultado")
        print(f"Nº sedan: {sedan}")
        print()

    while True:
        print("qual automovel vc deseja saber?")
        print("1º bike   ")
        print("2º bus    ")
        print("3º sedan")
        print("retornar")
        opcao = int(input("opção: "))
        if opcao == 1:
            bike()
        elif opcao == 2:
            buss()
        elif opcao == 3:
            Sedan()
        else:
            return titulo;

def total_de_vitimas ():
    titulo("Total de mortos e feridos nos acidentes")
    print("-"*30)

    def mortos():
        num_mortos = 0

        for acidente in acidentes:
            if(acidente['NUMBER OF PERSONS KILLED']!= ""):
                num_mortos += int(acidente['NUMBER OF PERSONS KILLED'])
        print(f"Nº Mortos: {num_mortos}")
        print()
    def feridos():
        num_feridos = 0
        for acidente in acidentes:
            if(acidente['NUMBER OF PERSONS INJURED']!= ""):
                num_feridos += int(acidente['NUMBER OF PERSONS INJURED'])
        print(f"Nº feridos: {num_feridos}")
        print()
    while True:
        print("qual informação vc deseja saber?")
        print("1º mortos   ")
        print("2º feridos    ")
        print("retornar")
        opcao = int(input("opção: "))
        if opcao == 1:
            mortos()
        elif opcao == 2:
            feridos()
        else:
            return titulo;

carrega_arquivo()

while True:
    titulo("Estatística de Acidentes em NYC", "=")
    print("1. Acidentes por Ano")
    print("2. Acidentes Agrupados por Bairro")
    print("3. Acidentes envolvendo Bikes, Bus e Sedans")
    print("4. Nº de Mortos e Feridos nos Acidentes")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        acidentes_ano()
    elif opcao == 2:
        acidentes_bairro()
    elif opcao == 3:
        filtro_por_automovel()
    elif opcao == 4:
        total_de_vitimas()
    else:
        break