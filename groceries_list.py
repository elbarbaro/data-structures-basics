# Algoritmo que pregunta 10 frutas o verduras 
# y las almacena en lo que es nuestra canaste del mandado
# Se pueden repertir
# Ejemplo: Manzana, Uvas, uvas, Chayote, papa

MAX_ITEMS = 10
groceries = []

for count in range(MAX_ITEMS):
	item = input(f'Objeto {count + 1} de la lista: ')
	# Métodos de manejo de strings
	item_lower = item.lower()
	groceries.append(item_lower)

print('Tu mandado quedó: ')
print(groceries)

for grocery in groceries:
	print(grocery)