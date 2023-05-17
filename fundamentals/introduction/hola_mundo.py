# 1. TAREA: imprime "Hola, mundo" // OK
print("Hola, Mundo")

# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print("Hola",name)	# con una coma //OK
print("Hola "+ name)	# con un + //OK

# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hola ", name)	# con una coma // OK
print("Hola " + str(name))	# con una +	-- este debería arrojar un error! OK// Se le da el parametro STR


# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
comida = "Amo comer {}, y {}".format(fave_food1,fave_food2)
print(comida) # con .format() //OK --  Se crea una variable y se le pasa los parametros, para luego imprimir
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f //OK -- Se agrega la F a la cadena, luego se llama a las variables con {}
