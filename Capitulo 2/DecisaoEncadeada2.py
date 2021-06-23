nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_infectocontagiosa = input("Suspeita de doença contagiosa?")

while True:
    if doenca_infectocontagiosa.upper() == "SIM":
        print("Encaminhar o paciente para sala AMARELA")
        break
    elif doenca_infectocontagiosa.upper() =="NAO":
        print("Encaminhar o paciente para a sala BRANCA")
        break
    else:
        print("Responda a suspeita de doença infectocontagiosa")
        doenca_infectocontagiosa = input("Suspeita de doença contagiosa?")

if idade >= 65:
    print("Paciente com prioridade")
else:
    genero =  input("Digite o genero do paciente: ")
    if idade >=10 and genero.upper() == "Feminino":
        gravidez = input("Esta gravida?")
        if gravidez.upper() == "SIM":
            print("Paciente com prioridade")
        else:
            print("Paciente sem prioridade")
    else:
        print("Paciente sem prioridade")