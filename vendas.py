vendas = 10000
input('digite suas vendas: ')
if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 150 
elif vendas > 5000:
    bonus = 50        
else:
    bonus = 0
    
print('seu bonus é:', bonus)
