#1
nome = input("Qual é o seu nome??")
print(nome, "você é belo(a)!")

#2
numero01 = int(input("Qual é o primeiro número?"))
numero02 = int(input("Qual é o segundo número?"))

soma = numero01 + numero02
print("A soma é:",soma)
#3
preco1 = float(input("Qual é o preço do produto?"))
quantidade = int(input("Qual a quantidade de produtos que você irá levar?"))

valor_total = preco1 * quantidade
print("O valor total será de: R$", valor_total)
#4
preco2 = float(input("Qual é o preço do produto?"))
desconto = float(input("Qual é o desconto a ser aplicado (em %)?"))

valor_com_desconto = preco2 - preco2*(desconto/100)
print("O valor com desconto será de: R$", valor_com_desconto)
#5
salario = float(input("Qual é o salário?"))
aumento = float(input("Qual é o aumento a ser recebido (em %)?"))

salario_com_aumento = salario + salario*(aumento/100)
print("O salário após o aumento será de: R$", salario_com_aumento)
#6
produto1=28
produto2=43
produto= int(produto1*produto2)
print("O produto entre os valores é:", produto)
#7
n1=float(input("Qual é o primeiro número?"))
n2=float(input("Qual é o segundo número?"))
n3=float(input("Qual é o terceiro número?"))
media=(n1+n2+n3)/3
print("a média é:", media)
#8
numb=int(input("Qual o numero?"))
antecessor=numb-1
sucessor=numb+1
print("O numero foi", numb, "o antecessor é", antecessor, "o sucessor é",  sucessor)

#9
n_1=float(input("Qual é o primeiro número?"))
n_2=float(input("Qual é o segundo número?"))
n_3=float(input("Qual é o terceiro número?"))
n_4=float(input("Qual é o quarto número"))
mediaponderada=(n_1*1+n_2*2+n_3*3+n_4*4)/10
print("a média é:", mediaponderada)
#10
saldo=float(input("Qual é o seu saudo atual?"))
reajuste=saldo*0.025
novoSaldo=reajuste+saldo
print("seu saldo agora é: ", novoSaldo)
#11
valor= float(input("Qual o valor?"))
taxa=float(input("qual a taxa?"))
tempo=float(input("Quanto tempo?"))
prestacao = valor + (valor *(taxa/100) *tempo)

print(prestacao)
#12
number1=float(input("Qual o primeiro numero?"))
number2=float(input("Qual o segunbdo numero?"))
soma=number1+number2
subtracao=number1-number2
multiplicacao=number1*number2
divisao=number1/number2
resto=number1%number2

print("A soma é: ", soma, "A subtração é: ",subtracao, "A multiplicação é: ", multiplicacao, "A divisao é: ", divisao, "o resto é: ", resto)
#13
base= 8
altura=6
perimetro=base+base+altura+altura
area=base*altura
print(perimetro, area)
#14
base= 5
altura=10
area=(base*altura)/2
print(area)
#15
raio= 2
perimetro=2*3.14*raio
area=3.14*raio**2