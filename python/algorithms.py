def pila_demo():
    pila = []
    pila.append(0)
    pila.append(1)
    print("Pila:")
    print(pila)
    print("Remover y obtener elemento de pila:")
    print(pila.pop())
    print("Pila actual:")
    print(pila)
    print("Agregar elemento a pila:")
    pila.insert(1,1)
    print(pila)

def secuencia_demo():
    secuencia = [x for x in range(10)]
    print("Secuencia:")
    print(secuencia)
    secuencia_impar = [x for x in range(10) if x % 2 == 0]
    print("Secuencia de numeros impares:")
    print(secuencia_impar)

def matriz_demo():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    matriz_traspuesta = [[row[i] for row in matriz] for i in range(4)]
    print("Matriz traspuesta")
    for fila in matriz_traspuesta:
        print(fila)

def conjunto_demo():
    lista = ['a', 'b', 'c', 'd', 'c', 'c', 'a']
    print("Lista:")
    print(lista)
    conjunto = set(lista)
    print("Conjunto:")
    print(conjunto)

def ciclos_demo():
    auto = {'modelo': 'Mazda 3', 'anio': '2003', 'color': 'blanco'}
    print("Mostrar elementos de diccionario:")
    for llave, valor in auto.items():
        print(llave + ': ' + valor)

    print("Mostrar elementos enumerados:")
    for posicion, elemento in enumerate(['blanco', 'negro', 'azul', 'verde']):
        print(posicion, elemento)

    print("Mostrar elementos ordenados:")
    for elemento in sorted(['blanco', 'negro', 'azul', 'verde']):
        print(elemento)

if __name__ == "__main__":
    pila_demo()
    secuencia_demo()
    matriz_demo()
    conjunto_demo()
    ciclos_demo()
