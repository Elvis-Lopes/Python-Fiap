nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "Não"

if idade >= 65:
    prioridade = "Sim"
    print(f'paciente: {nome}\n'
          f'Idade: {idade} anos\n'
          f'Prioridade: {prioridade}')
else:
    print(f'paciente: {nome}\n'
          f'Idade: {idade} anos\n'
          f'Prioridade: {prioridade}')