#Declaramos una variable

try:
    archivo = open('prueba.txt', 'w', encoding='utf8' ) #La w es de write(escribir)
    archivo.write('Programamos con diferentes tipos de archivos, ahora en un archivo .txt\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e) 
finally: #siempre se ejecuta
    archivo.close()# Con close se cierra el archivo

#archivo.write('Todo quedo perfecto')<- Esta linea de codigo no se puede ejecutar por que el archivo ya esta cerrado

