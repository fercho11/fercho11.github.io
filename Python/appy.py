lista_elements = {
    "id" : "1",
    "nombre" : "Emmanuel",
    "apellido" : "Aguilar"
},{
    "id" : "2",
    "nombre" : "Omar",
    "apellido" : "Flores"
}

lista_element = []

def add_element():
    lista_elements 

def remove_element():
    pass

def show_element():
    pass

def show_elements():
    # print(lista_element)
    pass

def edit_element():
    pass



if _name_ == '_main_':
    menu = '''
    Implementacion de CRUD de Elementos:
    Elige una Opcion
    1 - Insertar
    2 - Mostrar todos
    3 - Buscar por ID
    4 - Editar
    5 - Eliminar
    6 - Salir
    '''
    while True:
        opcion = input(menu)
        if opcion == '1':
            print("Insertar Elemento")
        elif opcion == '2':
            print ("Mostrar todos los elementos")
        elif opcion == '3':
            print ("Bucar por ID")
        elif opcion == '4':
            print ("Editar Elemento")
        elif opcion == '5':
            print ("Eliminar Elemento")
        elif opcion == '6':
            print ("Bye")
            break;
        else:
            print ("Opcion incorrecta")