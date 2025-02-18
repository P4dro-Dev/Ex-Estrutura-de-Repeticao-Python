cont_pares = 0 
cont_impares = 0 

for i in range(10): 
    numero = int(input("Número:"))
    if numero % 2 == 0:
        cont_pares = cont_pares + 1
    else: 
        soma_impares = soma_impares + numero

print(f"Qtde de números pares:{cont_pares}")
print(f"Quantidade de números ímpares:{soma_impares}")