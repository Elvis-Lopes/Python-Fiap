nivel_de_acesso = input("Digite o seu nivel de acesso: ")
genero = input("Digite o seu sexo: ")

if nivel_de_acesso.upper() == "ADM":
    if genero.upper() == "FEMININO":
        print("Bem-vindo administradora")
    else:
        print("Bem-vindo administrador")
elif nivel_de_acesso.upper() == "USER":
    if genero.upper() == "FEMININO":
        print("Olá usuaria")
    else:
        print("Olá usuario")
elif nivel_de_acesso.upper() == "GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
