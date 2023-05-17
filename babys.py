import csv
babys = []


def carrega_dados():
    with open("babys_name.csv", mode="r", encoding="utf-8")as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            babys.append(linha)


def titulo(texto, sublinhado='-'):
    print()
    print(texto)
    print(sublinhado*40)


def compare():
    print()
    titulo("compara nomes")

    Name_1 = input("1º Nome: ").upper()
    Name_2 = input("2º Nome: ").upper()

    total_Name1 = 0
    total_Name2 = 0

    print(f"\nNome: {Name_1}")
    print('-' * 30)

    for baby in babys:
        if baby["Child's First Name"].upper() == Name_1:
            print(
                f"{baby['Year of Birth']} {baby['Ethnicity']:30} {int(baby['Count']):4}")
            total_Name1 += int(baby['Count'])
    print(f"Total............: {total_Name1}")
    print(f"Nome: {Name_2}")
    print("-"*30)

    for baby in babys:
        if baby["Child's First Name"].upper() == Name_2:
            print(
                f"{baby['Year of Birth']} {baby['Ethnicity']:30} {int(baby['Count']):4}")
            total_Name2 += int(baby['Count'])
    print(f"Total.......: {total_Name2}")

def baby_female():
    titulo("Nomes do sexo feminino")

    female = 0

    for baby in babys:
            if"FEMALE" in baby[f"Gender"].upper():
                female +=1
    print()
    print(f"Nomes por sexo feminino: {female}")
    print("-"*30)

def baby_male():
    titulo("Nomes do sexo masculino")

    male = 0

    for baby in babys:
        if"MALE" in baby[f"Gender"].upper():
                male +=1
    print()
    print(f" sexo masculino: {male}")
    print("-"*30)

def destaque():
    titulo("Top 20")

    diccionario = {}

    for baby in babys:
        num = diccionario.get(baby["Child's First Name"].upper(), None)
        if num is None:
            diccionario[baby["Child's First Name"].upper()] = int(baby["Count"])
        else:
            diccionario[baby["Child's First Name"].upper()] = num + int(baby["Count"])

    lista = sorted(diccionario.items(), key=lambda dic: dic[1], reverse=True)

    print("\nNº Nome........: Total ")

    for ordem ,(nome, total) in enumerate(lista, start=1):
        print(f"{ordem:2d} {nome:20} {total}")
        if ordem == 20:
            break

carrega_dados()

while True:
    titulo("Nomes mais populares de bebes")
    print("1 - comparativo de nomes ")
    print("2 - Nomes femininos          ")
    print("3 - Nomes masculinos        ")
    print("4 - Top 20º nomes              ")
    print("5 - finalizar                          ")
    opcao = int(input("opção: "))

    if opcao == 1:
        compare()
    elif opcao == 2:
        baby_female()
    elif opcao == 3:
        baby_male()
    elif opcao == 4:
        destaque()
    else:
        break
