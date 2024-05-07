#RETO 11 - Parte 2
"""Desarrolle un programa que permita realizar el producto de matrices.
El programa debe validar las condiciones necesarias para ejecutar la operación.
"""

def tipo_producto() -> int:
    #Se consideran los tipos de sumas de matrices que existen
    print("Marque 1 para producto de una matriz por un escalar // 2 para producto de dos matrices // 3 para producto de Kronecker")
    tipo : int = int(input("Ingrese el tipo de producto de matrices que desea ejecutar: "))
    return tipo

def tipo_matriz() -> int:
    #El usuario decide cómo ejecutar el código
    print("Marque 1 para matriz ingresada por consola // 2 para matriz del programa")
    tipo : int = int(input("Ingrese el tipo de matriz que desea usar: "))
    return tipo

def introducir_dos_matrices():
    #Matriz A
    num_filas_A : int = int(input("Ingrese el número de filas de la matriz A: "))
    num_columnas_A : int = int(input("Ingrese el número de columnas de la matriz A: "))
    matriz_A : list = []
    for i in range(num_filas_A):
        fila_A : list = []
        for j in range(num_columnas_A):
            fila_A.append(float(input(f"Ingrese el elemento de matriz A la fila {i+1} columna {j+1}: ")))
        matriz_A.append(fila_A)
    #Matriz B
    num_filas_B : int = int(input("Ingrese el número de filas de la matriz B: "))
    num_columnas_B : int = int(input("Ingrese el número de columnas de la matriz B: "))
    matriz_B : list = []
    for k in range(num_filas_B):
        fila_B : list = []
        for l in range(num_columnas_B):
            fila_B.append(float(input(f"Ingrese el elemento de matriz B la fila {k+1} columna {l+1}: ")))
        matriz_B.append(fila_B)
    return matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B

def introducir_matriz_escalar():
    #Matriz A
    num_filas_A : int = int(input("Ingrese el número de filas de la matriz A: "))
    num_columnas_A : int = int(input("Ingrese el número de columnas de la matriz A: "))
    matriz_A : list = []
    for i in range(num_filas_A):
        fila_A : list = []
        for j in range(num_columnas_A):
            fila_A.append(float(input(f"Ingrese el elemento de matriz A la fila {i+1} columna {j+1}: ")))
        matriz_A.append(fila_A)
    #Escalar
    escalar : float = float(input("Ingrese el escalar: "))
    return matriz_A,escalar

def producto_escalar_matriz(escalar, matriz):
    # Inicializamos una lista vacía para almacenar la matriz resultante
    matriz_resultante = []
    
    # Iteramos sobre cada fila de la matriz
    for fila in matriz:
        # Inicializamos una lista vacía para almacenar la fila resultante
        fila_resultante = []
        # Iteramos sobre cada elemento de la fila y lo multiplicamos por el escalar
        for elemento in fila:
            fila_resultante.append(elemento * escalar)
        # Agregamos la fila resultante a la matriz resultante
        matriz_resultante.append(fila_resultante)
    
    return matriz_resultante

def producto_matriz_matriz(
        matriz_A : list, matriz_B : list, num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    #Se verifica que sea posible realizar el producto
    if num_columnas_A == num_filas_B:
        matriz_resultante : list = [[0] * num_columnas_B for _ in range(num_filas_A)]

        # Calcular el producto de las matrices
        for i in range(num_filas_A):
            for j in range(num_columnas_B):
                for k in range(num_columnas_A):
                    matriz_resultante[i][j] += matriz_A[i][k] * matriz_B[k][j]
        return matriz_resultante
    #Si no es posible se pide que se vuelvan a ingresar los datos únicamente por consola
    else:
        print("No es posible realizar la operación con las matrices proporcionadas.")
        print("Intente nuevamente")
        matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
        producto_matriz_matriz(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)

def producto_kronecker(matriz_A : list, matriz_B : list, num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    #Producto matriz A ⊕ matriz identidad de B
    matriz_resultado_1 = []
    for i in range(num_filas_A):
        fila_resultado = []
        for j in range(num_filas_B):
            for k in range(num_columnas_A):
                for l in range(num_columnas_B):
                    fila_resultado.append(matriz_A[i][k] * matriz_B[j][l])
            matriz_resultado_1.append(fila_resultado)
            fila_resultado = []
    return matriz_resultado_1

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
    print("Programa para el producto de matrices")
    while True:
        tipo_de_producto : int = tipo_producto()
        #Producto de un escalar por una matriz
        if tipo_de_producto == 1:
            tipo_de_matriz : int = tipo_matriz()
            #Datos introducidos por consola
            if tipo_de_matriz == 1:
                matriz,escalar = introducir_matriz_escalar()
                matriz_resultante : list = producto_escalar_matriz(escalar,matriz)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz)
                print(f"Escalar: {escalar}")
                print("Resultado del producto (A * B):")
                imprimir_matriz(matriz_resultante)
            
            #Datos de código
            elif tipo_de_matriz == 2:
                escalar : float = 4
                matriz : list = [
    [1, 10, 19, 28],
    [9, 18, 27, 29],
    [17, 26, 35, 37],
    [25, 34, 36, 45],
    [33, 42, 44, 4],
    [41, 43, 3, 12]
]
                matriz_resultante : list = producto_escalar_matriz(escalar,matriz)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz)
                print(f"Escalar: {escalar}")
                print("Resultado del producto (A * B):")
                imprimir_matriz(matriz_resultante)
            #En caso de que se ingrese un dato no válido
            else:
                print("SintaxError")
                
        #Producto de dos matrices
        elif tipo_de_producto == 2:
            tipo_de_matriz : int = tipo_matriz()
            #Datos introducidos por consola
            if tipo_de_matriz == 1:
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultante : list = producto_matriz_matriz(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz_A)
                print("Matriz B:")
                imprimir_matriz(matriz_B)
                print("Resultado del producto (A * B):")
                imprimir_matriz(matriz_resultante)
            #Matrices en el código
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [1, 10, 19],
    [9, 18, 27],
    [17, 26, 35]
]
                matriz_B : list = [
    [1, 10, 19],
    [9, 18, 27],
    [17, 26, 35]
]
                #Se miden las dimensiones de las matrices
                num_filas_A : int = len(matriz_A)
                num_columnas_A : int = len(matriz_A[0])
                num_filas_B : int = len(matriz_B)
                num_columnas_B : int = len(matriz_B[0])
                matriz_resultante : list = producto_matriz_matriz(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz_A)
                print("Matriz B:")
                imprimir_matriz(matriz_B)
                print("Resultado del producto (A * B):")
                imprimir_matriz(matriz_resultante)
        #Producto de kronecker
        elif tipo_de_producto == 3:
            tipo_de_matriz : int = tipo_matriz()
            #Datos introducidos por consola
            if tipo_de_matriz == 1:
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultante : list = producto_kronecker(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz_A)
                print("Matriz B:")
                imprimir_matriz(matriz_B)
                print("Resultado del producto (A ⊗ B):")
                imprimir_matriz(matriz_resultante)
            #Matrices en el código
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [1, 10, 19],
    [9, 18, 27],
    [17, 26, 35]
]
                matriz_B : list = [
    [2, 14, 25],
    [27, 59, 21],
    [26,31, 55]
]
                #Se miden las dimensiones de las matrices
                num_filas_A : int = len(matriz_A)
                num_columnas_A : int = len(matriz_A[0])
                num_filas_B : int = len(matriz_B)
                num_columnas_B : int = len(matriz_B[0])
                matriz_resultante : list = producto_kronecker(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)
                #Se imprimen las matrices junto con el resultado
                print("Matriz A:")
                imprimir_matriz(matriz_A)
                print("Matriz B:")
                imprimir_matriz(matriz_B)
                print("Resultado del producto (A ⊗ B):")
                imprimir_matriz(matriz_resultante)
        #El usuario decide si desea continuar
        opcion : int = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("SintaxError")
            break
        else:
            print("SintaxError")

# ! /\|=\/ 