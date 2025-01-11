# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:24:23 2024

@author: maria
"""

def restar_minimo_por_fila():
    global matriz
    matriz_final = []
    for fila in matriz:
        minimo = min(fila)
        nueva_fila = [x - minimo for x in fila]
        matriz_final.append(nueva_fila)
    matriz = matriz_final

def restar_minimo_por_columna():
    global matriz
    matriz_transpuesta = list(zip(*matriz))
    matriz_nueva = []
    for fila in matriz_transpuesta:
        minimo = min(fila)
        nueva_fila = [x - minimo for x in fila]
        matriz_nueva.append(nueva_fila)
    matriz = list(map(list, zip(*matriz_nueva)))

def marcar_ceros_y_obtener_columna():
    global matriz, columnas_cubiertas, lista_asteriscos
    filas, columnas = len(matriz), len(matriz[0])
    columnas_disponibles = list(range(columnas))
    filas_disponibles = list(range(filas))
    columnas_cubiertas = []
    lista_asteriscos = []
    for i in filas_disponibles[:]:
        for j in columnas_disponibles[:]:
            if matriz[i][j] == 0:
                lista_asteriscos.append((i, j))
                columnas_cubiertas.append(j)
                columnas_disponibles.remove(j)
                filas_disponibles.remove(i)
                break

def step_1():
    global matriz, columnas_cubiertas, lista_asteriscos, lista_apostrofes, filas_cubiertas
    filas, columnas = len(matriz), len(matriz[0])
    columnas_disponibles = list(range(columnas))
    filas_disponibles = list(range(filas))
    for k in columnas_cubiertas:
        columnas_disponibles.remove(k)
    for l in filas_cubiertas:
        filas_disponibles.remove(l)
    cambio, no_quedan, contador = True, False, 0
    while cambio:
        cambio = False
        for i in filas_disponibles[:]:
            for j in columnas_disponibles[:]:
                if matriz[i][j] == 0:
                    if (i, j) not in lista_apostrofes:
                        lista_apostrofes.append((i, j))
                    contador += 1
                    if i in filas_disponibles:
                        filas_disponibles.remove(i)
                    resultado = [x for x in lista_asteriscos if x[0] == i]
                    if resultado:
                        contador += 1
                        k = resultado[0][1]
                        filas_cubiertas.append(i)
                        filas_cubiertas.sort()
                        if k in columnas_cubiertas:
                            columnas_cubiertas.remove(k)
                            columnas_disponibles.append(k)
                            columnas_disponibles.sort()
                        cambio = True
                        break
                    else:
                        no_quedan = True
                        return no_quedan
    if contador % 2 == 0:
        return no_quedan
    no_quedan = True
    return no_quedan

def step_2():
    global lista_apostrofes, lista_asteriscos
    encontrado_apostrofe = lista_apostrofes[-1]
    while encontrado_apostrofe:
        _, valor_segundo = encontrado_apostrofe
        encontrado = None
        for elem in lista_asteriscos:
            if elem[1] == valor_segundo:
                encontrado = elem
                break
        if encontrado:
            lista_asteriscos.append(encontrado_apostrofe)
            lista_asteriscos.remove(encontrado)
            lista_apostrofes.remove(encontrado_apostrofe)
            valor_primero = encontrado[0]
            encontrado_apostrofe = None
            for elem in lista_apostrofes:
                if elem[0] == valor_primero:
                    encontrado_apostrofe = elem
                    break
        else:
            lista_asteriscos.append(encontrado_apostrofe)
            lista_apostrofes.remove(encontrado_apostrofe)
            return

def cubrir_columnas():
    global lista_asteriscos, columnas_cubiertas
    valores = [t[1] for t in lista_asteriscos]
    columnas_cubiertas = sorted(valores)

def calcular_minimo():
    global matriz, filas_cubiertas, columnas_cubiertas
    valores_validos = [
        matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz[0]))
        if i not in filas_cubiertas and j not in columnas_cubiertas
    ]
    return min(valores_validos)

def step_3():
    global matriz, filas_cubiertas, columnas_cubiertas
    fila = len(matriz)
    columna = len(matriz[0])
    minimo = calcular_minimo()
    for i in range(fila):
        for j in range(columna):
            if j not in columnas_cubiertas:
                matriz[i][j] -= minimo
            if i in filas_cubiertas:
                matriz[i][j] += minimo

def funcion_global():
    global matriz, columnas_cubiertas, lista_asteriscos, lista_apostrofes, filas_cubiertas
    restar_minimo_por_fila()
    restar_minimo_por_columna()
    marcar_ceros_y_obtener_columna()
    while True:
        if len(set(columnas_cubiertas) | set(filas_cubiertas)) == len(matriz):
            return
        else:
            A=step_1()
            if A:
                step_2()
                cubrir_columnas()
                filas_cubiertas = []
                lista_apostrofes = []
            else:
                step_3()

matriz=[[5,5,5],[10,1,2],[6,4,6]]
columnas_cubiertas = []
lista_asteriscos = []
lista_apostrofes = []
filas_cubiertas = []
funcion_global()
print( matriz,lista_asteriscos)



matriz=[[5, 5, 5, 20], [10, 1, 2, 1], [6, 4, 6, 10], [6, 4, 6, 10]]
columnas_cubiertas = []
lista_asteriscos = []
lista_apostrofes = []
filas_cubiertas = []
funcion_global()
print( matriz,lista_asteriscos)



matriz=[[5, 5, 5, 20, 15, 96, 1, 32], [10, 1, 2, 1, 8, 6, 14, 3], [6, 4, 6, 10, 7, 12, 11, 9], [6, 4, 6, 10, 10, 2, 9, 6], [8, 5, 2, 9, 7, 10, 23, 9], [5, 8, 5, 4, 5, 7, 5, 7], [8, 7, 4, 6, 5, 9, 10, 11], [14, 10, 12, 5, 2, 1, 3, 6]]
columnas_cubiertas = []
lista_asteriscos = []
lista_apostrofes = []
filas_cubiertas = []
funcion_global()
print( matriz,lista_asteriscos)

