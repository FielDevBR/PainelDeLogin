loginAdmin = "admin"
senhaAdmin = 12345
login = True

while (login):
  print("Bem Vindo Ao Sistema")
  loginlogin = input("Digite o Login: ")
  senha = int(input("Digite a senha (Somente Numeros): "))
  if senha == senhaAdmin and loginlogin == loginAdmin:
    print("Login efetuado com sucesso")
    login = False
    break

  elif loginlogin != loginAdmin:
    print("Login incorreto")
  
  elif senha != senhaAdmin:
    print("Senha incorreta")

else:
  print("Digite Algo Valido")
  