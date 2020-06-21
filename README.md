# Instrucciones

1. Has un fork de este repositorio dentro de tu cuenta personal.
2. Clona el repositorio creado en tu perfil.
3. Realiza el ejercicio propuesto con el nombre del archivo especificado. Deberás de verificar que cumplen con lo solicitado, además de utilizar buenas prácticas.
4. Una vez que termines los archivos, sube tus cambios a tu cuenta personal de Github.
5. Posteriomente, haz un Pull Request de tu cuenta personal a este repositorio, agregando como reviewer al instructor.

# Ejercicio

## Introducción
Necesitamos desarrollar un programa de consola para un restaurant que quiere tener un mini administrador de sus platillos que prepara y vende.

## Requerimientos
- Se utilizará Programación Orientada a Objetos

- Se requiere tener por cada platillo, la siguiente información:
  - Nombre del platillo
  - Descripción
  - Precio de preparación
  - Precio de venta
  - Ingredientes necesarios para elaborar (lista)
  - Tiempo de preparación (min)
  - Cantidad de calorias (kcal)

- En el menú inicial se tendrán las siguientes opciones:
    1. Ver platillos disponibles
    2. Buscar platillo por nombre
    3. Crear nuevo platillo
    4. Editar platillo existente
    5. Eliminar platillo
    6. Salir del programa

- En `Ver platillos disponibles` podremos ver todos los platillos que se han creado (cada platillo debe de ser una instancia de la clase, idear una manera de poner mantener dichas instancias).

- En `Buscar platillo por nombre` se le pedirá al usuario ingresar el nombre de un platillo. Si el platillo existe, mostrará la información del platillo. Si no existe ningún platillo con ese nombre, indicar que no existe.

- En `Crear nuevo platillo` se le pedirá todos los datos especificados en el punto dos al usuario necesarios para crear un platillo. Validad que donde se requiera introducir valores numéricos sean realmente números y no letras.

- En `Editar platillo existente` el usuario podrá ingresar el nombre de una platillo, si existe, se le pedirá que introduzca el atributo a actualizar (ejemplo: tiempo de preparación), y posteriormente, su nuevo valor. Indicar que los cambios se realizaron correctamente.

- En `Eliminar platillo` introducirá el nombre de un platillo. si este existe se eliminará la instancia, si no existe, indicarle al usuario que no existe dicho platillo.

- `Salir del programa`: Cerrar el programa.

## Notas extras

- Después de realizarse cualquier acción, deberá de mostrar nuevamente el menú principal, hasta que el usuario desee salir.

- Se recomienda el uso de funciones para modularizar el desarrollo.

- Nombre del archivo: `restaurant.py`
