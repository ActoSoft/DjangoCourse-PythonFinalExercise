global dishes
dishes = []

#DEFINO LOS ATRIBUTOS DEL PLATILLO
class Platillo:
    def __init__(self, name, description, recipe, investment, sell, time, kcal):
        self.name = name
        self.description = description
        self.recipe = recipe 
        self.investment = investment
        self.sell = sell
        self.time = time
        self.kcal = kcal 
    
        

def create_dish():

    name = input('Introduce el platilo nuevo: ')
    description = input('Introduce una descripción: ')
    recipe = input('Introduce los ingredientes: ')

    try: 

        investment = int(input('Introduce una inversión para realizar el platillo: '))

    except ValueError:
        print("El valor introducido debe ser un número entero")
        investment = int(input('Introduce una inversión para realizar el platillo: '))
            
    try: 

        sell = int(input('Introduce el precio al público: '))

    except ValueError:
        print("El valor introducido debe ser un número entero")
        sell = int(input('Introduce el precio al público: '))
    
    try: 

        time = int(input('Introduce el tiempo de preparación(min): '))

    except ValueError:
        print("El valor introducido debe ser un número entero")
        time = int(input('Introduce el tiempo de preparación: '))
    
    try: 

        kcal = int(input('Introduce las calorías del platillo (cal): '))

    except ValueError:
        print("El valor introducido debe ser un número entero")
        kcal = int(input('Introduce las calorías del platillo: '))
    
    platillo = Platillo(name, description, recipe, investment, sell, time, kcal)

    dishes.append(platillo)


def print_dishes():
    try:
        for dish in dishes:
        
            print (f'Platillo: {dish.name}. Descripción: {dish.description}. Inversión: ${dish.investment} MXN'
            f' Venta al público: ${dish.sell} MXN. Ingredientes: {dish.recipe}.'
            f' Tiempo de preparación: {dish.time}. Calorías en alimento: {dish.kcal}')
    
    except AttributeError:
        print('----------Hasta aquí es el menú--------')

def get_dish():
    
    user_dish = input('Ingresa el platillo  a buscar: ')
    for dish in dishes:

        if user_dish in dish.name:

            print (f'Platillo: {dish.name}. Descripción: {dish.description}. Inversión: ${dish.investment} MXN'
                f'Venta al público: ${dish.sell} MXN. Ingredientes: {dish.recipe}.'
                f'Tiempo de preparación: {dish.time}. Calorías en alimento: {dish.kcal}')
        
        else:

            print('No existe el platillo en el sistema')
    
       

def edit_dish():
    user_dish = input('Ingresa el platillo  a editar: ')

    for dish in dishes:
        if user_dish in dish.name:
            user_edit = int(input('¿Qué apartado desea editar?'
            '1. Descripcion 2. Inversion 3. Venta 4.Ingredientes'
            '5.Tiempo 6.Calorias: '))

            if user_edit == 1:
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print('Cambio exitoso')
        
            elif user_edit == 2:
                user_invest = input('Ingresa la nueva inversión: ')
                dish.investment = user_invest
                print('Cambio exitoso')

            elif user_edit == 3:
                user_sell = input('Ingresa el nuevo precio al público: ')
                dish.sell = user_sell
                print('Cambio exitoso')

            elif user_edit == 4:
                user_recipe = input('Ingresa los ingredientes: ')
                dish.recipe = user_recipe
                print('Cambio exitoso')

            elif user_edit == 5:
                user_time = input('Ingresa el nuevo tiempo: ')
                dish.time = user_time
                print('Cambio exitoso')

            elif user_edit == 6:
                user_kcal = input('Ingresa las nuevas calorías: ')
                dish.kcal = user_kcal
                print('Cambio exitoso')
            else:
                print('Esa opción no se encuentra disponible')
            
    
    
def erase_dish():
    user_dish = input('Ingresa el platillo  a eliminar: ')
    for dish in dishes:
        if user_dish in dish.name:
            del dish.name
            del dish.description
            print('Se ha borrado con éxito')
        
        else: 
            print('El platillo no existe')
    


def menu():
    print(" Seleciona las siguientes opciones\n 1. Ver platillos disonibles\n 2. Buscar platillos por nombre\n 3. Crear nuevo platillo\n 4. Editar platillo existente\n 5. Eliminar platillo\n 6. Salir del programa\n")
    user = int(input("Selecciona tu opción [1-6]: "))
    
    while user != 6:
        print(" Seleciona las siguientes opciones\n 1. Ver platillos disonibles\n 2. Buscar platillos por nombre\n 3. Crear nuevo platillo\n 4. Editar platillo existente\n 5. Eliminar platillo\n 6. Salir del programa\n")
        if user == 1:
            print_dishes()
        elif user == 2:
            get_dish()

        elif user == 3:
            create_dish()

        elif user == 4:
            edit_dish()

        elif user == 5:
            erase_dish()
        
        user = int(input("Selecciona tu opción [1-6]: "))

    else: 
        print('Hasta pronto')


menu()