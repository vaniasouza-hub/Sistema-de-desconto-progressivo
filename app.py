# --- ENTRADA DE DADOS ---
# Solicita que o usuário digite o valor total da compra e converte a resposta
# para o tipo 'float' (número decimal com casas decimais), armazenando-o na variável.
valor_total_da_compra= float(input("Digite valor total da compra: "))
# --- INICIALIZAÇÃO DE VARIÁVEL ---
# Define a variável 'percentual_desconto' com o valor inicial 0.0 antes do cálculo.
percentual_desconto=0.0
#  ESTRUTURA CONDICIONAL (REGRAS DE DESCONTO) ---
# Verifica em qual faixa de valor a compra se enquadra para definir a porcentagem de desconto:
# Se a compra for menor que R$ 200.00:
if valor_total_da_compra <= 200.00:
 percentual_desconto= 5.0 # Define a taxa em 0.5% 
 # Senão, se a compra for menor que R$ 300.00 
elif valor_total_da_compra <300.00:
 percentual_desconto= 10.0 # Define a taxa em 0.10%

else:
# Se a compra for de R$ 300.00 ou mais.
 percentual_desconto= 15.0 # Define a taxa em 0.15%

# Calcula o valor do desconto em reais aplicando a porcentagem obtida.
valor_do_desconto = valor_total_da_compra *  (percentual_desconto / 100)
# Subtrai o desconto do valor original para descobrir o valor final a ser pago
valor_atualizado= valor_total_da_compra - valor_do_desconto
# Imprime as mensagens formatadas na tela exibindo a porcentagem, o desconto e o valor final a pagar.
print(f"/Você recebeu um desconto de {percentual_desconto}%.")
print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Valor atualizado a pagar: R$ {valor_atualizado:.2f}")
