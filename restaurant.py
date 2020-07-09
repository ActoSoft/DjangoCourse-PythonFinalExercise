class Platillo:
    def __init__(self, nombre, descripcion, precio_preparacion, precio_venta, ingredientes, tiempo_preparacion, calorias):
        self.nombre = nombre 
        self.descripcion = descripcion
        self.precio_preparacion = precio_preparacion 
        self.precio_venta = precio_venta
        self.ingredientes = ingredientes
        self.tiempo_preparacion = tiempo_preparacion
        self.calorias = calorias

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion

    def get_precio_preparacion(self):
        return self.precio_preparacion
    
    def get_precio_venta(self):
        return self.precio_venta
        
    def get_ingredientes(self):
        return self.ingredientes
        
    def get_tiempo_preparacion(self):
        return self.tiempo_preparacion

    def get_calorias(self):
        return self.calorias


platillos = []
platillo_1 = {'Nombre':'spaguetti','descripcion':'es un pasta', 'precio_preparacion':50, 'precio_venta':60, 'ingredientes':['jitomate','ajo'], 'tiempo_preparacion':30, 'calorias':200}
platillos.append(platillo_1)
platillo_2 = {'Nombre':'arroz','descripcion':'es un cereal', 'precio_preparacion':30, 'precio_venta':40, 'ingredientes':['jitomate','cebolla'], 'tiempo_preparacion':20, 'calorias':150}
platillos.append(platillo_2)

#print(platillos[0])

def ver_platillos():
    for i in platillos:
    #print(i)
        print(i['Nombre'])
 
def buscar_platillo():
    contador = 0
    nombre_buscar = input('Ingresa el nombre del platillo que deseas buscar:')
    for i in platillos:
        if i['Nombre'] == nombre_buscar:
            print(f"Nombre: {i['Nombre']}\nDescripcion: {i['descripcion']}\nPrecio de preparación: {i['precio_preparacion']}\nPrecio de venta: {i['precio_venta']}\nIngredientes: {i['ingredientes']}\nTiempo de preparación: {i['tiempo_preparacion']}\nCalorias: {i['calorias']}")
            contador += 1
            break
        else:
            contador = 0
    if contador == 0: 
        print('Platillo no encontrado')        

def crear_platillo():
    nombre = input('Ingresa el nombre del platillo:')
    descripcion = input('Ingresa la descripcion del platillo:')
    print('Precio de preparación del platillo')
    precio_preparacion = validar_numeros()
    print('precio de venta del platillo')
    precio_venta = validar_numeros()

    ingredientes = []
    print('Cantidad de ingredientes')
    cant_ingre = validar_numeros()
    for i in range(0,cant_ingre):
        ingre = input('    Ingresa el ingrediente '+str(i+1)+': ')
        ingredientes.insert(i,ingre)

    print('Tiempo de preparacion en minutos')
    tiempo_preparacion = validar_numeros()
    print('Cantidad de calorias del platillo')
    calorias = validar_numeros()

    platillo = Platillo(nombre,descripcion,precio_preparacion,precio_venta,ingredientes,tiempo_preparacion,calorias)
    #print(f'El nuevo platillo es: {platillo.get_nombre()}')

    nuevo_platillo = {'Nombre':platillo.get_nombre(),
    'descripcion':platillo.get_descripcion(),
    'precio_preparacion':platillo.get_precio_preparacion(),
    'precio_venta':platillo.get_precio_venta(),
    'ingredientes':platillo.get_ingredientes(),
    'tiempo_preparacion':platillo.get_tiempo_preparacion(),
    'calorias':platillo.get_calorias()}

    platillos.append(nuevo_platillo)
    #print(platillos[2])

def editar_platillo():
    contador = 0
    indice_lista = 0
    nombre_buscar = input('Ingresa el nombre del platillo que deseas editar:')
    for i in platillos:
        indice_lista +=1
        if i['Nombre'] == nombre_buscar:
            contador += 1
            
            print('  1.Nombre\n  2.Descripción\n  3.Precio de preparacion\n  4.Precio de venta\n  5.Ingredientes\n  6.Tiempo de preparacion\n  7.Calorías\n  Ingresa el numero del dato que deseas modificar: ')
            opc = validar_numeros()

            if opc == 1:
                i['Nombre'] = input('Ingresa el nuevo nombre del platillo: ')
            elif opc == 2:
                i['descripcion'] = input('Ingresa la nueva descripcion del platillo: ')
            elif opc == 3:
                print('Nuevo precio de preparación')
                i['precio_preparacion'] = validar_numeros()
            elif opc == 4:
                print('Nuevo precio de venta')
                i['precio_venta'] = validar_numeros()
            elif opc == 5:
                try:
                    i['ingredientes'] = editar_ingredientes(i['ingredientes'])
                    print('datos actualizados correctamente')
                except:
                    print('hubo un error')
            elif opc == 6:
                print('Nuevo tiempo de preparación: ')
                i['tiempo_preparacion'] = validar_numeros()
            elif opc == 7:
                i['calorias'] = int(input('Ingresa la nueva cantidad de calorias: '))
            break
        else:
            contador = 0
    if contador == 0: 
        print('Platillo no encontrado')

def editar_ingredientes(lista_ingredientes):
    #print(lista_ingredientes)
    contador = 0
    for ingrediente in lista_ingredientes:
        contador += 1
        print(contador, ingrediente)

    print('Elige el ingrediente que deseas modificar')
    ingre_editar = validar_numeros()
    ingre_actualizado = input('Ingresa el nuevo valor del ingrediente: ')
    lista_ingredientes[ingre_editar-1] = ingre_actualizado
    return lista_ingredientes
 
def eliminar_platillo():
    contador = 0
    indice_lista = 0
    nombre_eliminar = input('Ingresa el nombre del platillo que deseas eliminar:')
    for i in platillos:
        indice_lista += 1
        if i['Nombre'] == nombre_eliminar:
            #print(f"Nombre: {i['Nombre']}\nDescripcion: {i['descripcion']}\nPrecio de preparación: {i['precio_preparacion']}\nPrecio de venta: {i['precio_venta']}\nIngredientes: {i['ingredientes']}\nTiempo de preparación: {i['tiempo_preparacion']}\nCalorias: {i['calorias']}")
            contador += 1
            del platillos[indice_lista-1]
            print('platillo eliminado')
            break
        else:
            contador = 0
    if contador == 0: 
        print('Platillo no encontrado')   

def validar_numeros():
    entrada = False
    while entrada == False:
        try:
            dato = int(input('    Ingresa el valor con números:'))
            entrada = True
            return dato
        except ValueError:
            print('    Valor incorrecto')
            entrada = False
        


option = 1

while option >=0 and option <6:
    print('\nBienvenido al sistema de restaurant\n',
    '*********************************\n', 
    '* 1. Ver platillos disponibles  *\n',
    '* 2. Buscar platillo por nombre *\n',
    '* 3. Crear nuevo platillo       *\n',
    '* 4. Editar platillo existente  *\n',
    '* 5. Eliminar platillo          *\n',
    '* 6. Salir del programa         *\n',
    '*********************************')

    try:
        option = int(input('Ingresa el número de la opción deseada:'))
    except ValueError:
        option = 0
    
    if option == 0:
        print('Valor incorrecto')
    elif option == 1:
        ver_platillos()
    elif option == 2:
        buscar_platillo()
    elif option == 3:
        crear_platillo()
    elif option == 4:
        editar_platillo()
    elif option == 5:
        eliminar_platillo()
    else:
        option = -1