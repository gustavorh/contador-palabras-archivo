# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:40:50 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def contar_palabras(nombre_archivo):
    # Se abre el archivo con el nombre ingresado por teclado.
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        # Se leen los datos dentro del archivo de una sola vez y se almacenan en la variable 'datos_leidos'.
        datos_leidos = archivo.read()

        # Se deben dividir las oraciones en palabras usando el siguiente método. split() es usado para dividir cada oración dentro de 'datos_leidos'
        # y toda esa información se guarda en la variable 'palabras'.
        palabras = datos_leidos.split()

        # Finalmente, se debe contar el largo de la variable que contiene las oraciones ya divididas en palabras
        cantidad_palabras = len(palabras)
    # El return entregará el valor final de palabras dentro del archivo de texto.
    return cantidad_palabras


# Se pregunta al usuario por el nombre del archivo y su extensión.
nombre_archivo = input(
    "Ingrese el nombre del archivo y su extensión (Ejemplo.txt): ")
# Se llama a la función pasando como parámetro el nombre del archivo ingresado por teclado.
numero_palabras = contar_palabras(nombre_archivo)

# Se entrega el resultado final.
print(
    f"La cantidad de palabras que contiene el archivo '{nombre_archivo}' son {numero_palabras}")
