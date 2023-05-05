nombre = input("Ingrese el nombre del artículo: ")
codigo = int(input("Ingrese el código del artículo (1 o 2): "))
precio = float(input("Ingrese el precio original del artículo: "))

if codigo == 1:
    descuento = precio * 0.10
elif codigo == 2:
    descuento = precio * 0.20
else:
    print("Código de artículo no válido")

precio_descuento = precio - descuento

print("Nombre del artículo:", nombre)
print("Código del artículo:", codigo)
print("Precio original:", precio)
print("Precio con descuento:", precio_descuento)
