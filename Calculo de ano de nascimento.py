nome= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
saldo= float(input("Digite seu saldo: "))
per=int(input("Digite percentual:"))

print (nome,",você nasceu em: ",2023-idade)
print (nome,"o seu saldo é:",saldo)
print ("Seu saldo com",per,":",(saldo*per)/100+saldo)
print (f"Você {nome} que nasceu em {2023-idade} terá em saldo de {per}%, que será R${(saldo*per)/100+saldo}.")