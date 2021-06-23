inventario = []
resposta = "S"
while resposta == "S":
    equipamento = [input("Equipmento: "),
                   float(input("Valor: ")),
                   int(input("Numero Serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite 'S' para continuar: ").upper()

for elemento in inventario:
    print(f'Nome: {elemento[0]}\n'
          f'Valor: {elemento[1]}\n'
          f'Serial: {elemento[2]}\n'
          f'Departmento: {elemento[3]}')

busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print(f'Valor: {elemento[1]}\n'
              f'Seril: {elemento[2]}')

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print(f'Valor antigo: {elemento[1]}')
        elemento[1] = elemento[1] * 0.9
        print(f'Novo valor: {elemento[1]}')

serial = int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print(f'Nome: {elemento[0]}\n'
          f'Valor: {elemento[1]}\n'
          f'Serial: {elemento[2]}\n'
          f'Departamento: {elemento[3]}')