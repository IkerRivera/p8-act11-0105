# Iker Montoya 0105

# 1. Sintaxis básica de una función
def dar_bienvenida():
    print("¡Hola! Bienvenido al tutorial de Python.")

dar_bienvenida()

# 2. Parámetros, argumentos y retorno
def calcular_suma(num1, num2):
    total = num1 + num2
    return total

resultado_suma = calcular_suma(15, 25)
print(f"El resultado es: {resultado_suma}")

# 3. Parámetros con valores por defecto
def registrar_persona(nombre, genero="hombre"):
    return f"Usuario: {nombre} | Género: {genero}"

print(registrar_persona("Mateo"))
print(registrar_persona("Sofia", genero="mujer"))

# 4. Argumentos variables (*args y **kwargs)
def sumar_elementos(*valores):
    return sum(valores)

print("Suma total:", sumar_elementos(10, 20, 30, 40))

def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(perfil="hombre", cargo="desarrollador", nivel="avanzado")

# 5. Funciones Lambda
elevar_al_cuadrado = lambda n: n ** 2
print("El cuadrado de 6 es:", elevar_al_cuadrado(6))

# 6. Evaluación de criterios
def verificar_criterios(edad, genero, activo=True):
    if edad >= 18 and activo:
        condicion = "Apto / Adulto activo"
    else:
        condicion = "No cumple los criterios"
    
    return {
        "genero": genero,
        "edad": edad,
        "condicion": condicion
    }

resultado_evaluacion = verificar_criterios(edad=22, genero="hombre")
print(resultado_evaluacion)

# Último print solicitado
print("Iker Montoya 0105")