# 1_Retornara valor 5
def number_of_food_groups():
    return 5


print(number_of_food_groups())


# 2_Retornara un error por las comillas del texto con el valor 5
def number_of_military_branches():
    return 5


print(number_of_days_in_a_week_silicon_or_triangle_sides() +
      number_of_military_branches())


# 3_Retornara he imprimira 5
def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())


# 4_Retornara el 5
def number_of_fingers():
    return 5
    print(10)


print(number_of_fingers())


# 5_No imprimira nada ya que no hay valor
def number_of_great_lakes():
    print(5)


x = number_of_great_lakes()
print(x)


# 6_Sumara 1+2 y despues 2+3 imprimiendo la suma de los dos / me dio error por la definicion de la variable
def add(b, c):
    print(b+c)


print(add(1, 2) + add(2, 3))


# 7_Tomara esos dos valores en texto con el parametro de str valor 25
def concatenate(b, c):
    return str(b)+str(c)


print(concatenate(2, 5))


# 8_Se le asigna el valoe de 100 a b y que imprima si el valor b es menor imprime 10 si es menor imprime 5
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(number_of_oceans_or_fingers_or_continents())


# 9_Si el valor de B es menor a C mostrar el valor del return segun el parametro dado en el print con el valor/ print= 7, print=14 , print= 14 mas la suma daria con el valor 7 "21"
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) +
      number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))


# 10_Se realizara una suma de valores de B+C TOTAL 8
def addition(b, c):
    return b+c
    return 10


print(addition(3, 5))


# 11_Primero imprimira dos veces 500 de la variable B - Despues imorimira el valor dos veces 300 en la variable b dentro de la funcion
b = 500
print(b)


def foobar():
    b = 300
    print(b)


print(b)
foobar()
print(b)


# 12_Primero imprimira dos veces 500 de la variable B - Despues imorimira el valor dos veces 300 en la variable b dentro de la funcion con retorno no hace nada
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)


# 13_Primero imprimira dos veces 500 de la variable B - Despues imorimira el valor dos veces 300 en la variable b dentro de la funcion b= no hace nada
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
b = foobar()
print(b)


# 14_Funcion en valor 0 con la impresion del valor de cada Print 1,2,3
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


foo()


# 15_Imprime los mismos valores del print retorna los valores de 5 y 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)
