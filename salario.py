#Informações
salario = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalhou no mês? "))

#Calculo
calculo = salario * horas

#Exibição
print(f"Seu salário ao mês é: R$ {calculo:.2f}")