#  Registra o valor total gasto pelo cliente
valor_total_da_compra = float(input("Digite valor total da compra: "))
#Verifica o valor da compra para aplicar o desconto de 5%
if valor_total_da_compra < 200.00:
    print("Você recebeu um desconto de 5%.")
#Verifica o valor da compra para aplicar o desconto de 10%
elif 200.00 <= valor_total_da_compra < 300.00: 
    print("Você recebeu um desconto de 10%.")
    # Se a compra for 300 ou mais, aplica o desconto máxim0 de 15% 
else:  
    print("Você recebeu um desconto de 15%.")