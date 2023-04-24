# Manejo de Excepciones:

from NumerosIgualesExcepcion import NumerosIgualesExcepcion

try:
    10/0
except Exception as e:
    print(f'Ocurrió un Error: {e}')

# Procesamiento de excepciones:
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except Exception as e: 
    print(f'Ocurrió un Error: {e}')

print(f'El resultado es: {resultado}')
print('Seguimos...')

# Excepciones específicas:
resultado = None
a = 7
b = 5
try:
    resultado = a / b
except TypeError as e:  # Clases hijas
    print(f'TypeError-Ocurrió un Error: {type(e)}')
except ZeroDivisionError as e:  # Clases hijas
    print(f'ZeroDivisionError-Ocurrió un Error: {type(e)}')
except Exception as e:  # Clase generic
    print(f'Exception-Ocurrió un Error: {type(e)}')

print(f'El resultado es: {resultado}')
print('Seguimos...')

# Creando variables dentro del try:
resultado = None  # Variable global

try:
    a = int(input('Digite el primer número:'))
    b = int(input('Digite el segundo número:'))
    resultado = a / b
except TypeError as e:  # clases hijas
    print(f'TypeError-Ocurrió un Error: {type(e)}')
except ZeroDivisionError as e:  # Clases hijas
    print(f'ZeroDivisionError-Ocurrió un Error: {type(e)}')
except Exception as e:  # Clase generic
    print(f'Exception-Ocurrió un Error: {type(e)}')

print(f'El resultado es: {resultado}')
print('Seguimos...')

# Bloque else y final:
resultado = None  # variable global

try:
    a = 2
    b = 2
    # Usamos nuestra clase excepción
    if a == b:
        raise NumerosIgualesExcepcion('Son números Iguales ')  # raise Nos permite arrojar una excepción
    resultado = a / b
except TypeError as e:  # Clases hijas
    print(f'TypeError-Ocurrió un Error: {type(e)}')
except ZeroDivisionError as e:  # Clases hijas
    print(f'ZeroDivisionError-Ocurrió un Error: {type(e)}')
except Exception as e:  # Clase generic
    print(f'Exception-Ocurrió un Error: {type(e)}')
else:
    print("No se arrojo ninguna excepción")
finally:  # Siempre se ejecuta
    print('Ejecución del bloque finally')
print(f'El resultado es: {resultado}')
print('Seguimos...')
