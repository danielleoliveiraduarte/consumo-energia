input("Digite o nome do aparelho:  ")
info1 = float(input("Digite a potência do aparelho (em watts):  "))
info2 = float(input("Digite o tempo de uso diário (em horas):  "))
print("O consumo diário de energia do aparelho é: ", info1 * info2, "watts-hora")
consumo_mensal = info1 * info2 * 30
print("O consumo mensal de energia do aparelho é: ", consumo_mensal, "watts-hora")
valor_mensal = consumo_mensal * 0.75 / 1000
print("O custo mensal de energia do aparelho é: R$ ", valor_mensal)
