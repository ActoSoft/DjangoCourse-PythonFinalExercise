dishes = []
class Platillo:
   
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #self.investment = investment
        #self.sell = sell
        #self.recipe = recipe 
        #self.time = time
        #self.kcal = kcal 
    
    def __str__(self):
        return str(self.name)
        

def create_dish():
  
    selection = 'si'
    while selection == 'si':



        name = input('Introduce el platilo nuevo: ')
        description = input('Introduce una descripción: ')
        
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
            


        # platillo = Platillo(name) 
        dishes.append( Platillo(name, description) )
        selection = input('¿Quieres agregar otro platillo? ')
        selection = selection.lower()





def print_dishes():

    for dish in dishes: 
        print (f'Platillo: {dish.name}. Descripción: {dish.description}')
        #print (f'Platillo: {dish.name}. Descripción: {dish.description}. Inversión: ${dish.investment} MXN'
        #f'Venta al público: ${dish.sell} MXN'
        #)

def get_dish():
    user_dish = input('Ingresa el platillo  a buscar: ')
    for dish in dishes:
        if user_dish in dish.name:
            print(dish.name, dish.description)
        else:
            print('No existe el platillo en el sistema')
            question = input('¿Deseas introducir este nuevo platillo al sistema? [Si/No]')
            if question == 'Si':
                create_dish()
            else: 
                print('Se retorna al menú de inicio')
                show_menu()
       

def edit_dish():
    user_dish = input('Ingresa el platillo  a editar: ')
    for dish in dishes:
        if user_dish in dish.name:
            user_edit = input('¿Qué apartado desea editar?')
            if user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)
        
            elif user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)

            elif user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)

            elif user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)

            elif user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)

            elif user_edit == 'Descripcion':
                user_descript = input('Ingresa la nueva descripción: ')
                dish.description = user_descript
                print(dish.description)
            
            else:
                print('Esa opción no se encuentra disponible')
            
        else:
            print('No existe el platillo en el sistema')
    
    
def erase_dish():
    user_dish = input('Ingresa el platillo  a eliminar: ')
    for dish in dishes:
        if user_dish in dish.name:
            del dish.name
            print('Se ha borrado con éxito')
        else: 
            print('El platillo no existe')
    
create_dish()
erase_dish()
#edit_dish()
print_dishes()

'''     

def principal_menu():
    print(" Seleciona las siguientes opciones\n 1. Ver platillos disonibles\n 2. Buscar platillos por nombre\n 3. Crear nuevo platillo\n 4. Editar platillo existente\n 5. Eliminar platillo\n 6. Salir del programa\n")
    user = int(input("Selecciona tu opción [1-6]: "))
    if user == 1:

    def get_name(self):
        return self.name

def create_dish():
    
    dish = []
    selection = "si"

    while selection == "si":

        user_dish = input("Introduce un nuevo platillo:\n ")
        
        platillo = Platillo(user_dish)
        print(platillo.get_name())
        dish.append(user_dish)

        selection = input("¿Deseas introducir otro platillo? ")
        selection = selection.lower()


    menu['Dish'] = dish          
    
    print(dish)
    
    
    
    #user_description = input("Introduce su descripción:\n ")

   # def dispo_dish(self, *args):
    #    if platillo == 0:
     #       create_dish()
      #  else:
       #     return f'Se encuentran {} '



create_dish()
'''