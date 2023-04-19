#Declaramos una variable
try:
    archivo = open('prueba.txt','w',encoding='utf-8')#la w es de write (que significa escribir)
    archivo.write('Programamos con diferentes tipos de archivos,ahora en txt\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.closed()#Con esto se debe cerrar el archivo
#     archivo.write('Todo quedó perfecto'):Este es un error
