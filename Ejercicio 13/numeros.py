lista = []
cantidad = int(input("Cantidad: "))
mayor = 0
menor = 0
i = 1

while(cantidad > 0):
    numero = float(input("Numero #" + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1

mayor = max(lista)
menor = min(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)
print("Menor: ", menor)
