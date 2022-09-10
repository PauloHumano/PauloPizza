# Creacion lista_menu

cantidad_items = int(input('ingrese cantidad de items: '))


def creacion_menu(cantidad_items):

    lista_menu = []
    lista_precio = []

    for i in range(cantidad_items):
        menu = input('ingrese menu: ')
        lista_menu.append(menu)
        precio = float(input('ingrese precio: '))
        lista_precio.append(precio)

    return lista_menu, lista_precio


lista_menus, lista_precios = creacion_menu(cantidad_items)

indice = 0
print('este es el listado de precios')

for i in lista_menus:

    print(indice, end='\t')
    print(lista_menus[indice], end='\t')
    print('$', lista_precios[indice])
    indice = 1 + indice

archivo_menus = open('lista_menu.txt', 'w')
archivo_menus.write(lista_menus)

strings = [str(x) for x in lista_precios)

strings = open('lista_precios.txt', 'w')
strings.write('lista_precios= % s','w')

# lista_precios = open('lista_precios.txt','w')

# print(lista_menus)
# print(lista_precios)
