def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Numero Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite S para continuar")

def exibirInventario(lista):
    for elemento in lista:
        print(f'Nome: {elemento[0]}\n'
              f'Valor: {elemento[1]}\n'
              f'Serial: {elemento[2]}\n'
              f'Departamento: {elemento[3]}')

