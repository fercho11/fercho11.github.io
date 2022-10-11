lista_elements = {
    "id" : "1",
    "nombre" : "Fernando",
    "apellido" : "Castañeda"
},{
    "id" : "2",
    "nombre" : "Emmanuel",
    "apellido" : "Aguilar"
}

lista_element = []

def add_element():
   id = int (input('Ingresa el ID de la persona: '))
   name = input (f"\n Ingresa el nombe de la persona: ")
   last_name = input (f"\n Ingresa el apellido de la persona: ")
   person = {
    "id": id,
    "name": name,
    "last_name": last_name
   }
   lista_elements.append(person)
    #lista_elements.append ()

def remove_element():
    #for para buscar (puede buscar con find)
    #lista_elements.remove
    id = int (input('Ingresa el ID de la persona a Eliminar: '))
    found = find_element (id)
    print (found)
    aceptar = input("Estás seguro? (S/N)")
    if aceptar == "S":
        lista_elements.remove (found)
        print("Elemento Eliminado")

def find_element ():
    #for para buscar
    #return element
    found = {}
    for element in lista_elements:
        if element ['id'] == id:
            found = element
    return found

def show_elements():
    # print(lista_element)
    for element in lista_elements:
        for key, value in element.items():
            print (f"{key} -> {value}")
    pass

def edit_element():
    #for o find para buscar
    #editar
    id = int (input('Ingresa el ID del elemento a editar: '))
    found = find_element (id)
    print(found)




if __name__ == '__main__':
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
            add_element()
        elif opcion == '2':
            print ("Mostrar todos los elementos")
            show_elements()
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