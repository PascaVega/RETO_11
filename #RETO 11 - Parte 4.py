#RETO 11 - Parte 4 
"""Desarrollar un programa que sume los elementos de una columna dada de una matriz.
"""
def introducir_matriz():
    #Matriz
    num_filas : int = int(input("Ingrese el número de filas de la matriz: "))
    num_columnas : int = int(input("Ingrese el número de columnas de la matriz: "))
    matriz_A : list = []
    for i in range(num_filas):
        fila_A : list = []
        for j in range(num_columnas):
            fila_A.append(float(input(f"Ingrese el elemento de matriz A la fila {i+1} columna {j+1}: ")))
        matriz_A.append(fila_A)
    #Se introduce el número de columna a sumar
    print(f"Primera columna (1) hasta la última columna ({num_columnas})")
    num_especifico : int = int(input(f"Ingrese el número de columna que desea sumar: "))
    #Se verifica que la columna exista
    if num_especifico-1 > num_columnas:
        print("No existe esa columna")
        matriz, num_especifico = introducir_matriz()
        #Se suma la columna
        total : float = sumar_columna(matriz,num_especifico)
        #Se imprime el resultado
        print("La matriz:")
        imprimir_matriz(matriz)
        print(f"La suma de la columna {num_especifico} es {total}")
        imprimir_columna(matriz,num_especifico)
    else:
        return matriz_A,num_especifico

def sumar_columna(matriz : list, num_especifico : int) -> float:
    num = num_especifico -1
    suma_columna : float = 0
    #Sumar los elementos de la columna
    for fila in matriz:
        suma_columna += (fila[num])
    return suma_columna

def imprimir_columna(matriz : list, num_especifico : int):
    #Se separa la columna en otra lista para imprimirla
    num = num_especifico -1
    columna : list = []
    for fila in matriz:
        columna.append(fila[num])
    #Se imprime la columna
    print(columna)
    return

def imprimir_matriz(matriz):
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
            #Se ingresa la matriz y el número de columna
            matriz : list = []   
            matriz, num_especifico = introducir_matriz()
            #Se suma la columna
            total : float = sumar_columna(matriz,num_especifico)
            #Se imprime el resultado
            print("La matriz:")
            imprimir_matriz(matriz)
            print(f"La suma de la columna {num_especifico} es {total}")
            imprimir_columna(matriz,num_especifico)


        #En caso de que se quiera evaluar la lista que hay en el código
        elif tipo_lista == 2:
            matriz : list = [
    [30, 39, 48, 1],
    [38, 47, 7, 9],
    [46, 6, 8, 17],
    [5, 14, 16, 25]
]
            num_especifico : int = 3
            #Se suma la columna
            total : float = sumar_columna(matriz,num_especifico)
            #Se imprime el resultado
            print("La matriz:")
            imprimir_matriz(matriz)
            print(f"La suma de la columna {num_especifico} es {total}")
            imprimir_columna(matriz,num_especifico)

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