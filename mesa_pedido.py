import pickle

archivo_menus = open('lista_menu', 'rb')
lista_menus = pickle.load(archivo_menus)
archivo_menus.close()

archivo_precios = open('lista_precio', 'rb')
lista_precios = pickle.load(archivo_precios)
archivo_precios.close()

hacer_pedido=input('hacer_pedido?')
def creacion_pedido(hacer_pedido):

    lista_cantidad_pedido = []
    lista_item_pedido = []

    item_pedido = 1

    while item_pedido > 0:
        item_pedido = int(input('ingrese item_pedido: '))
        if item_pedido == 0:
            print('fin')
            break
        else:
            lista_item_pedido.append(item_pedido)
            cantidad_pedido = int(input('ingrese cantidad_pedido: '))
            lista_cantidad_pedido.append(cantidad_pedido)

    return lista_cantidad_pedido, lista_item_pedido


lista_cantidad_pedido, lista_item_pedido = creacion_pedido(hacer_pedido)

indice = 0
print('este es el listado de pedidos')

for i in lista_cantidad_pedido:

    print(indice, end='\t')
    print(lista_cantidad_pedido[indice], end='\t')
    print(lista_item_pedido[indice])
    indice = 1 + indice
