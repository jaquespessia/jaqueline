#ATV 1
# digitar minha idade 

#idade = int(input("Digite a sua idade: "))

#if idade >= 18:
   # print("Você é maior de idade.")
#else:
   # print("Você é menor de idade.")

#ATV 2
#numero = int(input("Digite um número inteiro: ")) 

#if numero > 0:
  #  print("O número é positivo.")
#elif numero < 0:
 #   print("O número é negativo.")
#else:
 #   print("O número é zero.")

#ATV 3
#for numero in range(10, 0, -1):
  #  print(numero)

#ATV 4
#numero = int(input("Digite o número: "))
#for i in range(1, 11):
 #   resultado = numero * i
  #  print(f"{numero} x {i} = {resultado}")

#ATV 5

#soma_total = 0

#while True:
  #  numero = int(input("Digite um número: "))
    
  #  if numero == 0:
   #     break
    
  #  soma_total += numero 

#print(f"A soma total dos números é: {soma_total}")

#ATV 6
#numero_secreto = 9

#print("Advinhe o número secreto!")

#while True:
  #  palpite = int(input("Digite seu número (entre 1 e 10): "))
    
    #if palpite == numero_secreto:
     #   print("Você acertou!")
      #  break
  #  elif palpite < numero_secreto:
  #      print("Esta longe!")
   # else:
     #   print("Esta perto!")

#print("Parabéns!")

#ATV 7
#lista_compras = ["bolacha", "uva", "suco"]

#print("\nLista Inicial:")
#print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")

#while True:
  #  novo_item = input("\nNovo item (ou 'sair' para encerrar): ").strip()
    
   # if novo_item.lower() == 'sair':
   #     break
        
   # if novo_item:
   #     lista_compras.append(novo_item)
   #     print("\nLista Atualizada:")
   #     print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")
#else:
#print("Digite um item")

#print("\nLista Final:", lista_compras)

#ATV 8
#numeros = [34, 6, 70, 82, 153]
#print(f"O maior número é: {max(numeros)}")