# Meu primeiro projeto Python!!
#
# print() = comando de saida
print("Alo mundo!")

# Quando quiser guardar uma string!
nome = "Adriana"
#Quando quiser guardar um número inteiro
idade = 20

#Exibir o meu nome (que está dentro da variável nome)
print(nome)

#Quando quiser exibir a frase "Minha idade é" completando com o conteúdo de variável idade
#print ("Meu nome é "+nome)
print("Minha idade é " + str(idade) + " anos")
print(f"Minha idade é {idade} anos")
print("Minha idade é {} anos".format(idade))

#Quando quiser exibir "Meu nome é ... e tenho ... anos" trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))
'''
Comentario em bloco

'''

#comando input(): quero permitir que o usuário digite algo
nome = input("Digite seu nome: ")

#pede a idade para o usuário "Qual sua idade?"
idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")

#comando de saída..exiba "sua idade é"
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o dobro da idade?
dobro = idade * 2 
print("O dobro da idade informada é {}".format(dobro))

