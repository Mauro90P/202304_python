""" # Ejericio 1 Orden desendente Cuenta regresiva: crea una función que acepte un número como
     entrada. Devuelve una lista nueva que cuente de uno en uno,
     desde el número (como elemento 0) hasta 0 (como último elemento). 
     Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0] """


def countdown(num):
    list = []
    for x in range(num, -1, -1):
        list.append(x)
    return list


resultado = countdown(5)
print(resultado)


# Ejericio 2 mprimir y devolver
def imp_dev(listNum):
    print(listNum[0])
    return listNum[1]


resultado = imp_dev([1, 2])
print(resultado)


# Ejericio 3
""" Primero más longitud: crea una función que acepte una lista y 
devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)"""


def primero_mas_longitud(long):
    list = long[0]
    list2 = len(long)
    result = list + list2
    return result


result2 = primero_mas_longitud([1, 2, 3, 4, 5])
print(result2)


# Ejericio 4
""" Valores mayores que el segundo: escribe una función que acepte una lista y 
cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, 
has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4] """


def valores_mayores_que_el_segundo(mayor):
    list = mayor[1]
    b1 = []
    for a in mayor:
        if a > list:
            b1.append(a)
    print(len(b1))
    if len(b1) > 2:
        return b1
    else:
        return False


print(valores_mayores_que_el_segundo([5, 2, 3, 2, 4, 1]))


# Ejericio 5
""" Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros:
tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al 
tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2] """


def length_and_value(num1, num2):
    results = []
    for d in range(0, num1):
        results.append(num2)
    return results


op1 = length_and_value(4, 7)
op2 = length_and_value(6, 2)
print(op1, op2)
