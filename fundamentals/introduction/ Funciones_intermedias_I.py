# 1_Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


# 1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]  # Este es una lista con dos objetos 0,1,2 - 0,1,2
x[1][0] = 15
print(x[1])

estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
# 2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0]['last_name'])

directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes['fútbol'])


z = [{'x': 10, 'y': 20}]
# Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z)


# 2-Iterar a través de una lista de diccionarios

# Crea una función iterateDictionary(some_list)para que, dada una lista
# de diccionarios, la función recorra cada diccionarios de la lista e imprima
# cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
#
# REALICE UNOS CAMBIOS PERO EN TODAS ME SALE EN VACIO EL RESULTAD HELP MEEEE

estudiantes = [{'first_name':  'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}, {
    'first_name': 'Mark', 'last_name': 'Guillen'}, {'first_name': 'KB', 'last_name': 'Tonel'}]


def iterateDictionary(estudiantes):
    for estudiante in estudiantes:
        for clave in estudiante:
            print(f"{clave} - {estudiante[clave]},", end=" ")
        print()


# 3-Obtener valores de una lista de diccionarios


# 4-Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo)
