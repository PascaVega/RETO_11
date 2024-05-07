# Reto_11
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th colspan="2"><b>Reto 11 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Para este ejercicio, se tiene en cuenta las diferentes tipos de adiciones de matrices existentes. Por lo cual, el programa permite ejecutar las sigueientes operaciones:</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Suma/Resta por componentes:</b></td>
    <td style="color:#141414" align="center"><p>Es una operación en la que se suman los elementos correspondientes de matrices del mismo tamaño para formar una nueva matriz (del mismo tamaño).</p>
      <p><b>Condiciones:</b>
        <li>Ambas matrices deben de ser de igual tamaño.</li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Suma directa:</b></td>
    <td style="color:#141414" align="center"><p>Es una operación que combina las dos matrices de forma tal que la matriz resultante tenga un tamaño igual a la suma de los tamaños de las matrices originales.</p>
      <p><b>Condiciones:</b>
        <li>Ambas matrices no tienen que ser de igual tamaño.</li>
        <li>Siendo la matriz A de tamaño <i>mxn</i> y la matriz B de tamaño <i>pxq</i>, la matriz resultante es de tamaño <i>(m+p)x(n+q)</i> </li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Suma de kronecker:</b></td>
    <td style="color:#141414" align="center"><p>Es una operación diferente que se aplica a matrices de diferentes tamaños, permitiendo combinarlas para formar una matriz más grande.</p>
      <p><b>Condiciones:</b>
        <li>Ambas matrices no tienen que ser de igual tamaño.</li>
        <li>Se define utilizando el producto Kronecker ⊗ y adición matricial normal.</li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Dado la extensión del código, únicamente se presentan las funciones de las operaciones específicas.</td>
  </tr>
</table>

**Suma por componentes** 
```python
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
```

**Suma Directa por componentes** 
```python
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
```

**Suma Kronecker** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th colspan="2"><b>Reto 11 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Para este ejercicio, se tiene en cuenta los diferentes tipos de productos de matrices existentes. Por lo cual, el programa permite ejecutar las sigueientes operaciones:</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Producto de una matriz por una escalar:</b></td>
    <td style="color:#141414" align="center"><p>Es una operación en álgebra lineal donde cada elemento de la matriz original se multiplica por el escalar dado.</p>
      <p><b>Condiciones:</b>
        <li>La matriz resultante es del mismo tamaño que la matriz operada.</li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Producto de una matriz por otra matriz:</b></td>
    <td style="color:#141414" align="center"><p>Se realiza una combinación lineal de las filas de la primera matriz con las columnas de la segunda matriz para obtener la matriz resultante.</p>
      <p><b>Condiciones:</b>
        <li>Ambas matrices no tienen que ser de igual tamaño, pero el número de columnas de la matriz 𝐴 tiene que ser igual al número de filas de la matriz B (operando <i>A * B</i>).</li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Producto kronecker:</b></td>
    <td style="color:#141414" align="center"><p>Es una operación entre dos matrices que resulta en una matriz más grande que se construye a partir de bloques de la matriz original.</p>
      <p><b>Condiciones:</b>
        <li>Dadas dos matrices 𝐴 y B, el producto de Kronecker, se denota como A⊗B.</li>
        <li>Ambas matrices no tienen que ser del mismo tamaño.</li></p> </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center" colspan="2">Dado la extensión del código, únicamente se presentan las funciones de las operaciones específicas.</td>
  </tr>
</table>

**Multiplicación de una matriz por un escalar** 
```python
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
```

**Producto de una matriz por otra matriz** 
```python
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
```

**Producto Kronecker** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 11 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este ejercicio, se crea un programa en la que se intercambian las columnas por las filas para obtener la matriz transpuesta.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dada la extensión del código solo se presenta la función específica.</td>
  </tr>
</table>

**Matriz Transpuesta**
```python
def matriz_transpuesta(matriz : list) -> list:
    #Se separan las columnas en otra lista y se añaden a una nueva matriz como filas
    matriz_resultante : list = []
    num_columnas : int = len(matriz[0])
    for i in range(num_columnas):
        columna : list = []
        for fila in matriz:
            columna.append(fila[i])
        matriz_resultante.append(columna)
    return matriz_resultante
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrollar un programa que sume los elementos de una columna dada de una matriz.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se crea un programa para la suma de una columna específica, pero dada la extensión del código a continuación solo se presenta la función específica.</td>
  </tr>
</table>

**Suma de la columna**
```python
def sumar_columna(matriz : list, num_especifico : int) -> float:
    num = num_especifico -1
    suma_columna : float = 0
    #Sumar los elementos de la columna
    for fila in matriz:
        suma_columna += (fila[num])
    return suma_columna
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Al igual que en el punto anterior, se crea un programa para la suma de una fila específica, pero dada la extensión del código a continuación solo se presenta la función específica.</td>
  </tr>
</table>

**Suma de la fila** 
```python
def sumar_fila(matriz : list, num_especifico : int) -> float:
    num = num_especifico -1
    suma_fila : float = 0
    #Sumar los elementos de la fila
    fila : list = matriz[num]
    for elemento in fila:
        suma_fila += elemento
    return suma_fila
```

<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
            <tr>
                <th>Referencias</th>
            </tr>
            <tr>
                <td>Wikipedia. (s. f.). Adición matricial. En Wikipedia. Recuperado de https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial<a href="https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial"></a></td>
            </tr>
            <tr>
                <td>Wikipedia. (s. f.). Multiplicación de matrices. En Wikipedia. Recuperado de https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices <a href="https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices"></a></td>
            </tr> 
            <tr>
                <td>Wikipedia. (s. f.). Matriz transpuesta. En Wikipedia. Recuperado de https://es.wikipedia.org/wiki/Matriz_transpuesta<a href="https://es.wikipedia.org/wiki/Matriz_transpuesta"></a></td>
            </tr> 
            <tr>
                <td>Wikipedia. (s. f.). Producto de Kronecker. En Wikipedia. Recuperado de https://es.wikipedia.org/wiki/Producto_de_Kronecker<a href="https://es.wikipedia.org/wiki/Producto_de_Kronecker"></a></td>
            </tr> 
        </table>
    </div>
