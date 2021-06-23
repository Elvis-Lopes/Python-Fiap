equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar").upper()

for indice in range(0, len(equipamentos)):
    print(f'Equipamento: {equipamentos[indice]}\n'
          f'Valor: {valores[indice]}\n'
          f'Serial: {seriais[indice]}\n'
          f'Departamento: {departamentos[indice]}')

busca = input("Digite o nome do equipamento que deseja buscar: ")
decisao = int(input("1- Drepreciar \n"
                    "2- apagar"))
if decisao == 1:
    for indice in range (0, len(equipamentos)):
        if busca == equipamentos[indice]:
            valores[indice] = valores[indice] - (valores[indice]*10)/100
            print(f'Valor: {valores[indice]}\n'
                  f'Serial: {seriais[indice]}')
elif decisao == 2:
    for indice in range(0, len(equipamentos)):
        if busca == equipamentos[indice]:
            del equipamentos[indice]
print(equipamentos)