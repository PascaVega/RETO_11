#RETO 11 - Parte 3
"""Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada.
El programa debe validar las condiciones necesarias para ejecutar la operación.
"""
def introducir_matriz():
    #Matriz
    num_filas : int = int(input("Ingrese el número de filas de la matriz: "))
    num_columnas : int = int(input("Ingrese el número de columnas de la matriz: "))
    matriz : list = []
    for i in range(num_filas):
        fila : list = []
        for j in range(num_columnas):
            fila.append(float(input(f"Ingrese el elemento de matriz A la fila {i+1} columna {j+1}: ")))
        matriz.append(fila)
    return matriz

def matriz_transpuesta(matriz : list):
    #Se separan las columnas en otra lista y se añaden a una nueva matriz como filas
    matriz_resultante : list = []
    num_columnas : int = len(matriz[0])
    for i in range(num_columnas):
        columna : list = []
        for fila in matriz:
            columna.append(fila[i])
        matriz_resultante.append(columna)
    return matriz_resultante

def imprimir_matriz(matriz : list):
    #Se imprime la matriz
    for fila in matriz:
        for elemento in fila:
            # Imprime el elemento seguido de una tabulación
            print(elemento, end="\t")
        # Imprime una nueva línea al final de cada fila
        print()
    return 

def continuar() -> int:
    #El usuario decide si desea repetir el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (Sí) o 2 (No): "))
    return opcion

if __name__ == "__main__":
    #Inicia el programa
    print("Programa para sumar los elementos de una columna dada de una matriz")
    #El programa se repetira tantas veces como el usuario lo desee
    while True:
        #Se inicia con el usuario decidiendo si desea ingresar la matriz por la consola o tomar la matriz que está en el código
        tipo_lista : int = int(input(
            "Ingrese el tipo de matriz que desea utilizar. Marque 1 (lista ingresada por consola) o 2(lista en código): "))
        #En caso de que la lista la ingrese por consola
        if tipo_lista == 1:
            #Se ingresa la matriz
            matriz : list = []   
            matriz = introducir_matriz()
            #Se suma transpone la matriz
            matriz_resultante : list = matriz_transpuesta(matriz)
            #Se imprime el resultado
            print("La matriz:")
            imprimir_matriz(matriz)
            print(f"La matriz transpuesta es:")
            imprimir_matriz(matriz_resultante)


        #En caso de que se quiera evaluar la lista que hay en el código
        elif tipo_lista == 2:
            matriz : list = [
    [30, 39, 48, 1],
    [38, 47, 7, 9],
    [46, 6, 8, 17],
    [5, 14, 16, 25]
]
            #Se suma transpone la matriz
            matriz_resultante : list = matriz_transpuesta(matriz)
            #Se imprime el resultado
            print("La matriz:")
            imprimir_matriz(matriz)
            print(f"La matriz transpuesta es:")
            imprimir_matriz(matriz_resultante)

        #En caso de que el usuario ingrese una opción no válida
        else:
            print("SintaxError")

        #El usuario decide si desea continuar
        opcion : int = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("SintaxError")
            break

# ! /\|=\/ 