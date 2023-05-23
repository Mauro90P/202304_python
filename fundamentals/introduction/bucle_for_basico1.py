""" Básico: imprime todos los números enteros del 0 al 150. """

for x in range(0, 151):
    print(x)
print("**"*20)

# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for x in range(5, 1001, 5):
    print(x)

# Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for x in range(1, 101):
    if x % 5 == 0:
        print(x)
        print("coding")
    if x % 10 == 0:
        print(x)
        print("coding dojo")

    print("coding Dojo")
print("**"*20)
for x in range(1, 101):
    if x % 10 == 0:
        print(x)
        print("coding dojo")
    elif x % 5 == 0:
        print(x)
        print("coding")
print("**"*20)

# 4 Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
e = 0
for d in range(0, 500000):
    if d % 2 == 1:
        e = e + d
print("La suma total es ", e)
print("**"*20)
""" print(6% 2==0) """

# 5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
num = 2018
for s in range(2, num+1, 4):
    print(s)

# 6 Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
owNum = 3
highNum = 9
mult = 3
otro = 6
numero = [owNum, highNum, otro]
res = mult * owNum
res1 = mult * highNum
res2 = mult * otro
# mostrando los valores de la multiplicacion del valor matris "mult"
print(res, res1, res2)
print(numero[2]*mult, numero[1]*mult, numero[0]*mult)  # multiplicacion desc
