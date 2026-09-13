valor_total_da_compra = float(input("Digite valor total da compra: "))

if valor_total_da_compra < 200.00:
    print("Você recebeu um desconto de 5%.")
elif 200.00 <= valor_total_da_compra < 300.00: 
    print("Você recebeu um desconto de 10%.")
else:  
    print("Você recebeu um desconto de 15%.")