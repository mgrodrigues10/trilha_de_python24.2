dado_nome = str(input('Digite seu nome:'))

print(dado_nome.capitalize())

dado_cpf = input('Digite seu CPF:')
if len(dado_cpf) < 9:
    print('CPF invalido') 
elif len(dado_cpf)>9:
    print('CPF inválido')
else:
    print('CPF registrado com sucesso:' , dado_cpf)
#print(list(cpf))

dado_senha = input('Digite sua senha (Deve conter ABC,123,!@#$%*):')
sim = ["@","#","!","$","%*"]

if len(dado_senha) <= 4:
    print('Senha fraca')
elif dado_senha.isalpha() or dado_senha.isnumeric() or dado_senha.isalnum():
   print("senha errada")

else:  
    for c in dado_senha:
        
        if not c.isalpha() and not c.isnumeric():
            if c in sim: 
                print("senha correta")
            else:
                print("senha incorreta")


