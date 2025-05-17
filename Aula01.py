 #Uma loja de departamentos deseja criar um algoritmo para calcular o preço final de um produto após a aplicação de descontos progressivos, de acordo com a quantidade comprada. As regras de desconto são as seguintes: 

quant = int(input("Quantas peças?"))

preço = float(input('Qual o preço da unidade?'))

total = quant * preço

#Se o cliente comprar até 10 unidades, o preço por unidade será mantido. 
if quant <= 10:
    print('R$', total)
#Se o cliente comprar entre 11 e 20 unidades, haverá um desconto de 5% no preço unitário. 
elif quant <= 20:
    total1 = total * 0.95 
    print('R$' , total1 )
#Se o cliente comprar entre 21 e 50 unidades, o desconto será de 10%.
elif quant <= 50:
    total2 = total * 0.90
    print('R$', total2)
#Se o cliente comprar mais de 50 unidades, o desconto será de 20%.
elif quant > 50:
    total3 = total * 0.80
    print('R$', total3)
#Além disso, se o valor final da compra (já com desconto) for superior a R$ 500,00, o cliente receberá um bônus adicional de 5% de desconto sobre o valor total. 
elif total3 > 500:
    total4 = total3 * 0.95
    print( 'R$' , total4 )


 



#Leia o preço do produto e a quantidade comprada. 
#Calcule corretamente o valor total a pagar após aplicar os descontos conforme as regras acima. 
#Exiba o valor final a ser pago pelo cliente. 
