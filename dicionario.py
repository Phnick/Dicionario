# # Criação de um dicionário é usado para armazenar dados
cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
# #Acessar uma chave do dicionário que no cso se chama 'Matricula', logo apos o print, o resultado e 22222
print(cadastro['Matricula'])


# #Atualizar o dicionário

cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
cadastro['Turma']= '2g'
print(cadastro)

# # Agora iremos adicionar um novo dado no dicionário
cadastro['Modalidade']= 'EAD'
print(cadastro)


# # pop() remove um item do dicionário

cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
print(cadastro.pop('Turma'))
print(cadastro)

# # Métodos de consultas no dicionário items() retorna os dois juntos
cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
print(cadastro.items())

# # Método keys() retorna a penas as chaves
cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
print(cadastro.keys())

# # Método values() retorna os valores das chaves
cadastro ={'Matricula': 222222,
           'Dia_cadastro': 25,
           'Mes cadastro' : 10,
           'Turma': '2e'}
print(cadastro)
print(cadastro.values())


# ##
loja ={'nomes':['televisão', 'celular', 'notebook'],
       'precos': [2000, 3000, 1300]}
print(loja)


for chave, elementos in loja.items():
    print(f'chave:{chave}\nElemntos: ')
    for dado in elementos:
        print(elementos)


## Desafios

lista ={3000, 1000, 2000, 5000}
media = sum(lista)/len(lista)
print(media)

# Desafio 2
lista ={3000, 1000, 2000, 5000}
contador = 0
for gasto in lista:
    if gasto > 3000:
        print(gasto)
        contador +=1
        print(contador)

# Desafio 3

lista = [1,2,3,4,5]   
print(lista)   


# Desafio 4

lista = []

for i in range(0,5):
    numero = int(input('Insira um número inteiro: '))
    lista.append(numero)


    print(f'lista de número invertida {lista[::-1]}')


animais = ['Gato','Macaco','Passaro']

for animal in animais:
     animal = str(input('Digite um nome de um animal: '))
     if animal in animais:
         print(f'O {animal} está na lista {animais}')
         break
     else:
         print(f'O {animal} não esta na lista {animais}')



sala =[]

for aluno in range (0,5):
    aluno = str(input('Digite seu nome'))
    sala.append(aluno)
    print(sala)
   






