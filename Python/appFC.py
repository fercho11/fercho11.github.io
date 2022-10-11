def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Balon adidas', accion1),
        '2': ('Guantes de portero Nike', accion2),
        '3': ('Tenis adidas predator', accion3),
        '4': ('Espinilleras Nike Mercurial', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has comprado Balon adidas')


def accion2():
    print('Has comprado Guantes de portero Nike')


def accion3():
    print('Has comprado Tenis adidas predator')

def accion4():
    print('Has comprado Espinilleras Nike Mercurial ')

def salir():
    print('Gracias por tu compra')

if _name_ == '_main_':
    menu_principal()