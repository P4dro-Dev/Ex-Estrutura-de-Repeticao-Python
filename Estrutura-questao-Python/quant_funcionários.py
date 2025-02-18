qunt_funcionarios = int(input("Qual a quantidade de funcionários?"))
soma = 0

for i in range(qunt_funcionarios):
   salario = float(input("Qual o salário dos funcionários?"))
   soma = soma + salario

media = soma / qunt_funcionarios
print(f"Total da folha de pagamento: {soma}")
print(f"Média de salários: {media}")

    
    
