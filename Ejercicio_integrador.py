respuesta = input('BienvEnid@, ¿Desea comenzar? \n [S/N] ' )
while respuesta != 's' and respuesta != 'n':
    respuesta = input('ERROR. Ingrese una opcion correcta. \n [S/N] ' )
    
mensaje_final = 'GRACIAS POR UTILIZAR EL PROGRAMA. '

lista_productos = []
lista_precios = []
lista_unidades = []
lista_fabricantes = []
acumulador_barbijo_max = 0
acumulador_unidades_jabon = 0
unidades_max = None
barbijo_max = None

while respuesta == "s":
    ####VALIDACION PRODUCTOS####
    producto = input('Ingrese tipo de producto [BARBIJO/JABON/ALCOHOL] ')
    producto = producto.upper()
    while producto != "BARBIJO" and producto != "JABON" and producto != "ALCOHOL":
        producto = input('Ingrese un producto válido [BARBIJO/JABON/ALCOHOL]')
        producto = producto.upper()
    lista_productos.append(producto)
    ####VALIDACION PRECIOS####
    precio = input('Ingrese el precio. [100 - 300] ')
    precio = int(precio)
    while precio < 100 or precio > 300  :
        precio = input('Ingrese un precio válido. ')
        precio = int(precio)
    lista_precios.append(precio)
    ####VALIDACION UNIDADES####
    unidades = input('Ingrese la cantidad unidades. [0 - 1000] ')
    unidades = int(unidades)
    while unidades < 0 or unidades > 1000 :
        unidades = input('Ingrese cantidad unidades válidas. ')
        unidades = int(unidades)
    lista_unidades.append(unidades)
    ####VALIDACION FABRICANTES####
    fabricante = input('Ingrese el fabricante. ')
    fabricante = fabricante.capitalize()
    while fabricante == "":
        fabricante = input('Error. Ingrese el fabricante. ')
        fabricante = fabricante.capitalize()
    lista_fabricantes.append(fabricante)
    
    respuesta =input('¿Desea continuar? [S/N] ')

for i in range(len(lista_productos)): 
    unidades = lista_unidades[i]
    if lista_productos[i] == 'BARBIJO':
        precio_barbjo = lista_precios[i]        
        unidades_barbijo = lista_unidades[i]        
        acumulador_barbijo_max += unidades_barbijo
        if barbijo_max == None or barbijo_max < precio_barbjo:
            barbijo_max = precio_barbjo
    elif lista_productos[i] == 'JABON':
        unidades_jabon = lista_unidades[i]
        acumulador_unidades_jabon += unidades_jabon
    
    if unidades_max == None or unidades_max < unidades:
        unidades_max = unidades
        fabricante_max = lista_fabricantes[i]  

print(f'Produto: {lista_productos}')
print(f'Precios: {lista_precios}')
print(f'Unidades: {lista_unidades}')
print(f'Fabricante: {lista_fabricantes}')

if barbijo_max == None:
    print('No hay barbijos')
else:
    print(f'EL barbijo mas caro es: {barbijo_max}')
    print(f'Cantidad de barbijos mas caros: {acumulador_barbijo_max}')

""" if acumulador_barbijo_max <= 0 :
    print(f'No hay barbijos')  """

if unidades_max == None :
    print('No hay stock')
else:
    print(f'El item con mas unidades tiene: {unidades_max} y su fabricante es {fabricante_max}')

if acumulador_unidades_jabon <= 0:
    print('No hay stock de jabones.')
else:
    print(f'La cantidad de jabones que hay en total es: {acumulador_unidades_jabon}')


print(mensaje_final)