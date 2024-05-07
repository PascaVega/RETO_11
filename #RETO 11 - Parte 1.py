#RETO 11 - Parte 1
""""Desarrolle un programa que permita realizar la suma/resta de matrices. 
El programa debe validar las condiciones necesarias para ejecutar la operación.
"""
def tipo_suma() -> int:
    #Se consideran los tipos de sumas de matrices que existen
    print("Marque 1 para suma por componentes // 2 para resta por componentes // 3 para suma directa // 4 par suma Kronecker")
    tipo : int = int(input("Ingrese el tipo de adición de matrices que desea ejecutar: "))
    return tipo

def tipo_matriz() -> int:
    #El usuario decide cómo ejecutar el código
    print("Marque 1 para matriz ingresada por consola // 2 para matriz del programa")
    tipo : int = int(input("Ingrese el tipo de maatriz que desea usar: "))
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

def imprimir_matriz(matriz : list):
    #Se imprime la matriz
    for fila in matriz:
        for elemento in fila:
            # Imprime el elemento seguido de una tabulación
            print(elemento, end="\t")
        # Imprime una nueva línea al final de cada fila
        print()
    return  

def suma_componentes(
        matriz_A : list, matriz_B : list,num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    matriz_resuelta : list = suma_matrices(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)
    #Se imprimen las matrices junto con el resultado
    print("Matriz A:")
    imprimir_matriz(matriz_A)
    print("Matriz B:")
    imprimir_matriz(matriz_B)
    print("Resultado de la suma de componentes (A + B):")
    imprimir_matriz(matriz_resuelta)
    return

def suma_matrices(
        matriz_A : list, matriz_B : list, num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    if num_filas_A == num_filas_B and num_columnas_A == num_columnas_B:
        #Se suman los componentes
        matriz_resultado : list = []
        for p in range(num_filas_A):
            fila :  list = []
            for q in range(num_columnas_A):
                elemento_suma : float = matriz_A[p][q] + matriz_B[p][q]
                fila.append(elemento_suma)
            matriz_resultado.append(fila)
        return matriz_resultado

    else:
        print("No es posible realizar la operación con las matrices proporcionadas.")
        print("Intente nuevamente")
        matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
        suma_matrices(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)

def resta_componentes(
        matriz_A : list, matriz_B : list,num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    if num_filas_A == num_filas_B and num_columnas_A == num_columnas_B:
        #Se suman los componentes
        matriz_resultado : list = []
        for p in range(num_filas_A):
            fila :  list = []
            for q in range(num_columnas_A):
                elemento_suma : float = matriz_A[p][q] - matriz_B[p][q]
                fila.append(elemento_suma)
            matriz_resultado.append(fila)
        #Se imprimen las matrices junto con el resultado
        print("Matriz A:")
        imprimir_matriz(matriz_A)
        print("Matriz B:")
        imprimir_matriz(matriz_B)
        print("Resultado de la resta (A - B):")
        imprimir_matriz(matriz_resultado)
        return

    else:
        print("No es posible realizar la operación con las matrices proporcionadas.")
        print("Intente nuevamente")
        matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
        suma_matrices(matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B)

def tamaño_matriz(matriz : list):
    """"#Se mide cada linea de la matriz para asegurar que la matriz sea posible de trabajar,
    al tiempo que dse mide la cantidad de elementos.
    """
    num_filas : int = len(matriz)
    num_columnas : int = 0
    valor_base : int = len(matriz[0])
    for r in range(num_filas):
        num_columnas = len(matriz[0])
        if num_columnas !=  valor_base:
            print("No es posible trabajar con la matriz.")
            break
    return num_filas,num_columnas

def suma_directa(
        matriz_A : list, matriz_B : list,num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    matriz_resultado : list  = []
    print("Matriz A:")
    imprimir_matriz(matriz_A)
    print("Matriz B:")
    imprimir_matriz(matriz_B)
    for a in range(num_filas_A):
        fila : list = matriz_A[a]
        for b in range(num_columnas_B):
            fila.append(0)
        matriz_resultado.append(fila)
    for c in range(num_filas_B):
        fila : list = matriz_B[c]
        for d in range(num_columnas_A):
            fila.insert(0,0)
        matriz_resultado.append(fila)
    
    print("Resultado de la suma directa (A ⊕ B):")
    imprimir_matriz(matriz_resultado)
    return

def suma_kronecter(
        matriz_A : list, matriz_B : list,num_filas_A : int, num_columnas_A : int, num_filas_B : int, num_columnas_B : int):
    #Primero se calcula el producto kronecter con las respectivas matrices identidad para ambas matrices
    matriz_identidad_A : list = matriz_identidad(num_filas_A,num_columnas_A)
    matriz_identidad_B : list = matriz_identidad(num_filas_B,num_columnas_B)

    num_filas_matriz_identidad_A : int = len(matriz_identidad_A)
    num_columnas_matriz_identidad_A : int = len(matriz_identidad_A[0])
    num_filas_matriz_identidad_B : int = len(matriz_identidad_B)
    num_columnas_matriz_identidad_B : int = len(matriz_identidad_B[0])

    #Producto matriz A ⊕ matriz identidad de B
    matriz_resultado_1 = []
    for i in range(num_filas_A):
        fila_resultado = []
        for j in range(num_filas_matriz_identidad_B):
            for k in range(num_columnas_A):
                for l in range(num_columnas_matriz_identidad_B):
                    fila_resultado.append(matriz_A[i][k] * matriz_identidad_B[j][l])
            matriz_resultado_1.append(fila_resultado)
            fila_resultado = []

    #Producto Matriz identidad de A ⊕ matriz B
    matriz_resultado_2 = []
    for i in range(num_filas_matriz_identidad_A):
        fila_resultado = []
        for j in range(num_filas_B):
            for k in range(num_columnas_matriz_identidad_A):
                for l in range(num_columnas_B):
                    fila_resultado.append(matriz_identidad_A[i][k] * matriz_B[j][l])
            matriz_resultado_2.append(fila_resultado)
            fila_resultado = []

    #Se miden las dimensiones de las matrices resultantes
    num_filas_1 : int = len(matriz_resultado_1)
    num_columnas_1 : int = len(matriz_resultado_1[0])
    num_filas_2 : int = len(matriz_resultado_2)
    num_columnas_2 : int = len(matriz_resultado_2[0])

    #Se suman las dos matrices y se imprimen
    matriz_resuelta : list = suma_matrices(matriz_resultado_1,matriz_resultado_2,num_filas_1,num_columnas_1,num_filas_2,num_columnas_2)
    #Se imprimen las matrices junto con el resultado
    print("Matriz A:")
    imprimir_matriz(matriz_A)
    print("Matriz B:")
    imprimir_matriz(matriz_B)
    print("Resultado de la suma de Kronecker(A ⊕ B):")
    imprimir_matriz(matriz_resuelta)
    return

def matriz_identidad(num_filas : int, num_columnas : int):
    matriz_resultante : list = []
    for i in range(num_filas):
        # Inicializamos una fila vacía
        fila = []
        # Iteramos sobre el número de columnas
        for j in range(num_columnas):
            # Si el índice de fila es igual al índice de columna, agregamos 1, de lo contrario, agregamos 0
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        # Agregamos la fila a la matriz identidad
        matriz_resultante.append(fila)
    return matriz_resultante
    
def continuar() -> int:
    #El usuario decide si desea repetir el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (Sí) o 2 (No): "))
    return opcion

if __name__ == "__main__":
    #Inicia el programa
    print("Programa para adición y sustración de matrices")
    #El programa se repetira tantas veces como el usuario lo desee
    while True:
        tipo_de_suma : int = tipo_suma()
        num_filas_A : int = 0
        num_filas_B : int = 0
        num_columnas_A : int = 0
        num_columnas_B : int = 0

        #Suma de componentes
        if tipo_de_suma == 1:
            tipo_de_matriz : int = tipo_matriz()
            #Matriz ingresada por consola
            if tipo_de_matriz == 1:
                matriz_A : list = []
                matriz_B : list = []
            
                #Se introducen las matrices
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma y se ejecuta
                suma_componentes(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [30, 39, 48, 1],
    [38, 47, 7, 9],
    [46, 6, 8, 17],
    [5, 14, 16, 25],
    [13, 15, 24, 33],
    [21, 23, 32, 41]
]
                matriz_B : list = [
    [1, 10, 19, 28],
    [9, 18, 27, 29],
    [17, 26, 35, 37],
    [25, 34, 36, 45],
    [33, 42, 44, 4],
    [41, 43, 3, 12]
]
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma
                num_filas_A,num_columnas_A = tamaño_matriz(matriz_A)
                num_filas_B,num_columnas_B = tamaño_matriz(matriz_B)
                #Se verifica que sea posible hacer la suma y se ejecuta
                suma_componentes(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)

        #Resta de componentes
        if tipo_de_suma == 2:
            tipo_de_matriz : int = tipo_matriz()
            #Matriz ingresada por consola
            if tipo_de_matriz == 1:
                matriz_A : list = []
                matriz_B : list = []
            
                #Se introducen las matrices
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma y se ejecuta
                resta_componentes(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [30, 39, 48, 1],
    [38, 47, 7, 9],
    [46, 6, 8, 17],
    [5, 14, 16, 25],
    [13, 15, 24, 33],
    [21, 23, 32, 41]
]
                matriz_B : list = [
    [1, 10, 19, 28],
    [9, 18, 27, 29],
    [17, 26, 35, 37],
    [25, 34, 36, 45],
    [33, 42, 44, 4],
    [41, 43, 3, 12]
]
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma
                num_filas_A,num_columnas_A = tamaño_matriz(matriz_A)
                num_filas_B,num_columnas_B = tamaño_matriz(matriz_B)
                ##Se verifica que sea posible hacer la suma y se ejecuta
                resta_componentes(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)

        #Suma directa
        elif tipo_de_suma == 3:
            tipo_de_matriz : int = tipo_matriz()
            #Matriz ingresada por consola
            if tipo_de_matriz == 1:
                matriz_A : list = []
                matriz_B : list = []
            
                #Se introducen las matrices
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultado : list = []
                #Se ejecuta la suma
                suma_directa(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [30, 39],
    [38, 47]
]
                matriz_B : list = [
    [1, 10, 19],
    [9, 18, 27]
]
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma
                num_filas_A,num_columnas_A = tamaño_matriz(matriz_A)
                num_filas_B,num_columnas_B = tamaño_matriz(matriz_B)
                #Se ejecuta la suma directa
                suma_directa(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)
        
        #Suma Kronecker
        elif tipo_de_suma == 4:
            tipo_de_matriz : int = tipo_matriz()
            #Matriz ingresada por consola
            if tipo_de_matriz == 1:
                matriz_A : list = []
                matriz_B : list = []
            
                #Se introducen las matrices
                matriz_A,matriz_B,num_filas_A,num_columnas_A,num_filas_B,num_columnas_B = introducir_dos_matrices()
                matriz_resultado : list = []
                #Se ejecuta la suma
                suma_kronecter(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)
            elif tipo_de_matriz == 2:
                matriz_A : list = [
    [1,2],
    [3,4]
]
                matriz_B : list = [
    [5,6,7],
    [8,9,10],
    [11,12,13]
]
                matriz_resultado : list = []
                #Se verifica que sea posible hacer la suma
                num_filas_A,num_columnas_A = tamaño_matriz(matriz_A)
                num_filas_B,num_columnas_B = tamaño_matriz(matriz_B)
                #Se ejecuta la suma directa
                suma_kronecter(matriz_A,matriz_B,num_filas_A, num_columnas_A, num_filas_B, num_columnas_B)

        #El usuario decide si desea continuar
        opcion : int = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("SintaxError")
            break

# ! /\|=\/ 