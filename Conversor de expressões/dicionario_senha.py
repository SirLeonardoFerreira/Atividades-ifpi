passwordDictionary = {
    "programador" : "acesso"
    }
loginAttempts = 0
while loginAttempts < 3:
    name = input("Nome: ").lower()
    senha = input("Senha: ").lower()
    if name in passwordDictionary and senha == passwordDictionary[name]:
        print("BEM-VINDO PROGRAMADOR")
        break
    else:
        print("Senha errada, tente novamente!")
        loginAttempts += 1

if loginAttempts == 3:
    print("Usuário bloqueado, tentativas sucessivas de acesso negado!")



