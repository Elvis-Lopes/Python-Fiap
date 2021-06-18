nome = input("Digite o seu nome: ")
empresa = input("Digite o nome da sua empresa: ")
qtde_funcionarios = int(input("Insira a quantidade de funcionario: "))
media_mensalidade = float(input("valor da Mensalidade "))

print(f'\n{nome} trabalha na empresa {empresa}\n'
      f'Possui {qtde_funcionarios} funcionarios\n'
      f'A média da mensalidade é de: R$ {media_mensalidade}')