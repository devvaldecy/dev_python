# Exemplo Básico !!!
#print("Olá Mundo !!!") # Linha de comentários

#Imprimindo duas variaveis
'''
nome  = "Valdecy Silva"
idade = 49
print("Nome",nome,"Idade",idade)
print("Nome " +nome,"Idade "+str(idade) )
#f_string formatação
print(f"Nome {nome} idade {idade}")
CL
# Combinando variáveis e texto
x     = 3
y     = 6
total = x+y
print("A soma de",x,"mais",y, "é igual",total)
print("A soma de",x,"mais",y, "é igual",x+y)

# Separadores
print("Valdecy","Sousa","Silva")
print("Valdecy","Sousa","Silva",sep=';')
print("Valdecy","Sousa","Silva",sep=',')

# Agurmento and
print("Eu sou valdecy")
print("da empresa valdecy info",end=' ')
print("Valdecy","Sousa","Silva",sep=',')

# imprimindo uma lista de frutas

frutas = ["laranja","caju","Goiaba"]

print("frutas.:",frutas)

#Impriminto uma função com join
print("Frutas,: "+" - ".join(frutas))

for i in range(5):
    print("Index ",i,"Valor ixi", i*i)

'''
for i in range(5):
    print(f"Indice {i} valor {i*i}")