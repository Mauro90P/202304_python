num3 = 72  # Variable numerica
print(num3)  # Se imprime el valor de la variable con el dato asignado
num1 = 42  # Almacena un Entero
num2 = 2.3  # Almacena un flotante
boolean = True  # Declaracion de un booleano "verdadero"
print(boolean)  # Imprime TRUE
string = 'Hello World'  # Dato de texto literal de tipo cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives']  # Esto es una lista "Array"
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.
fruit = ('blueberry', 'strawberry', 'banana')  # Declaracion de una TUPLA
print(type(fruit))  # Imprime el tipo de dato de la clase TUPLE
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Imprime el segundo dato del arreglo que seria "SAUSAGE"
print(pizza_toppings[1])
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Se agrega al final del arreglo "Mushrooms"
pizza_toppings.append('Mushrooms')
print(pizza_toppings)
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.

# Imprime el valor que esta dentro del diccionario que seria "Jhon"
print(person['name'])
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.
# Actualiza el valor en la llave con el nuevo nombre "George"
person['name'] = 'George'
print(person)
# Asigna un nuevo dato en las llaves "Eye_color" con el dato "blue"
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.
person['eye_color'] = 'blue'
print(person)
fruit = ('blueberry', 'strawberry', 'banana')  # Declaracion de una TUPLA
# En esta tupla solo muestra lo que esta en la casilla n°2 "Banana"
print(fruit[2])


num1 = 42
if num1 > 45:
    print("It's greater")  # Aca esta la operacion de que si  num1 es mayor que 45, por lo que NO y nos mostrara "It' is lower" si num1 fuera num1= 50 nos mostraria el otro mensaje ya que que seria mayor que 45
else:
    print("It's lower")
print("**" * 20)

string = 'Hello World'  # Variable de texto de cadena
if len(string) < 5:  # Extrae el largo de la variable de texto del "String" si es menor a 5 muestra el mensaje que sigue pero como es mayor sigue el flujo del lopp
    # Si en el string acortamos el texto a tres letras nos mostraria el mensaje
    print("It's a short word!")
elif len(string) > 15:  # Si de lo contrario el valor string es > que 15 nos mostraria el mensaje "It's a long word!", pero como no es mas largo muestra el otro mensaje "Just right!"
    # Imprime el mensaje si el string fuera mayor 15
    print("It's a long word!")
else:
    print("Just right!")  # Imprime el valor de no cumplir que es mayor a 15.
print("**" * 20)  # Separacion de texto para orden

for x in range(5):  # Se inicia una variable x con un rango de largo 5
    print(x)  # Se imprime  x con el largo del rango de 0,1,2,3,4
print("**" * 20)  # Separacion de texto para orden
for x in range(2, 5):  # Se inicia en el rango en la posicion 2 de largo 5
    print(x)  # Imprime desde la posicion 2 hasta el 5 que es 4 segun (0,1,2,3,4)
print("**" * 20)  # Separacion de texto para orden
for x in range(2, 10, 3):  # Inicia el rango en posicion 2 de largo 10 con salto de linea 3
    # Imprime el orden de su posicion de 2 a salto de linea de 3 en 3 con largo 10 que mostra solo 8 por el salto de linea.
    print(x)
print("**" * 20)  # Separacion de texto para orden

x = 0  # Declaracion de varible numerica en 0
while (x < 5):  # Mientras x sea menor < que 5
    print(x)  # Imprime el valor de la opeacion
    x += 1  # Se le asigna el valor 1 para que finalice cuando sea mayor o igual
print("**" * 20)  # Separacion de texto para orden

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
pizza_toppings.pop()  # POP elimina el ultimo registro de la lista
print(pizza_toppings)

print("**" * 20)  # Separacion de texto para orden

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
pizza_toppings.pop(1)  # Elimina la posicion 1 de la lista "Souce"
print(pizza_toppings)

print("**" * 20)  # Separacion de texto para orden

person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.
print(person)  # Imprime todo la lista de lo que esta en esa variable

print("**" * 20)
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # Este es un diccionario de datos con grupos de valores.
person['eye_color'] = 'blue'  # Se le agrega el dato a la lista
print(person)
# El pop elimina el ultimo registro de la variable Person
person.pop('eye_color')
print(person)

print("**" * 20)

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
for topping in pizza_toppings:
    if topping == 'Sausage':
        continue
    # Imprime 4 mensajes de las pizzas restantes de la lista
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times():  # Imprime hola en 10
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):  # NO logre revelar lo que era
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):  # NO logre revelar lo que era
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #done
# num3 = 72 #done
# fruit[0] = 'cranberry' # en la clase tupla no se podra asignar en el valor 0 el cranberry
# print(person['favorite_team']) # NO existe ese dato por lo que no se mostrara nada
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry') # En la Tupla no se pueden agregar contenidos
# fruit.pop(1)  # En la tupla no se pueden eliminar registros establecidos
