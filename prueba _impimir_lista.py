import pickle

archivo_menus = open('lista_menu', 'rb')
lista_menus = pickle.load(archivo_menus)
print(lista_menus)
archivo_menus.close()

archivo_precios = open('lista_precio', 'rb')
lista_precios = pickle.load(archivo_precios)
print(lista_precios)
archivo_precios.close()
