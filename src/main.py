import argparse
import random

# Se crea un analizador de argumentos
parser = argparse.ArgumentParser()
# Se añade un argumento 'k' al analizador
parser.add_argument('k', type=int)
args = parser.parse_args()
k = args.k
matrixsize = 2**k
counter = 0
# Se inicializa una matriz de tamaño 'matrixsize' con todos los elementos como 0
matrix = [[0]*matrixsize for _ in range(matrixsize)]

def place(*coordinates):
    """
    Aumenta el contador y pone ese número en las posiciones dadas de la matriz.
    """
    global counter
    counter += 1
    for coordinate in coordinates:
        matrix[coordinate[0]][coordinate[1]] = counter

def neighbors(x, y):
    """
    Devuelve los números alrededor de una posición en la matriz.
    """
    surrounding = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x+i < matrixsize and 0 <= y+j < matrixsize and matrix[x+i][y+j] != -1:
                surrounding.add(matrix[x+i][y+j])
    return surrounding

def fillRegion(regionsize, x, y):
    """
    Esta es la función recursiva que se utiliza para llenar una región de la matriz con adoquines.
    """
    global counter
    r, c = next(((i,j) for i in range(x, x + regionsize) for j in range(y, y + regionsize) if matrix[i][j] != 0), (0, 0))
    if regionsize == 2:
        counter += 1
        for i in range(regionsize):
            for j in range(regionsize):
                if(matrix[x + i][y + j] == 0):
                    matrix[x + i][y + j] = counter
        return   
    mid_x, mid_y = x + regionsize // 2, y + regionsize // 2
    if r < mid_x and c < mid_y:
        place((mid_x, mid_y - 1), (mid_x, mid_y), (mid_x - 1, mid_y))
    elif r >= mid_x and c < mid_y:
        place((mid_x - 1, mid_y), (mid_x, mid_y), (mid_x - 1, mid_y - 1))
    elif r < mid_x and c >= mid_y:
        place((mid_x, mid_y - 1), (mid_x, mid_y), (mid_x - 1, mid_y - 1))
    elif r >= mid_x and c >= mid_y:
        place((mid_x - 1, mid_y), (mid_x, mid_y - 1), (mid_x - 1, mid_y - 1))

    fillRegion(regionsize // 2, x, y + regionsize // 2)
    fillRegion(regionsize // 2, x, y)
    fillRegion(regionsize // 2, x + regionsize // 2, y)
    fillRegion(regionsize // 2, x + regionsize // 2, y + regionsize // 2)

def start():
    """
    Esta función se utiliza para iniciar el proceso de adoquinamiento.
    """
    global matrix

    # Asignamos una posición aleatoria para el adoquín especial
    a = random.randint(0, matrixsize - 1)
    b = random.randint(0, matrixsize - 1)
    matrix[a][b] = -1
    fillRegion(matrixsize, 0, 0)

    for row in matrix:
        print(' '.join(map(lambda x: "{:3}".format(x), row)))

    # Buscar la posición del adoquín especial y mostrarla
    for i in range(matrixsize):
        for j in range(matrixsize):
            if matrix[i][j] == -1:
                surrounding = neighbors(i, j)
                print(f"\nEl adoquín especial está en la posición ({i+1}, {j+1}).")
                print(f"Está rodeado por los adoquines: {', '.join(map(str, surrounding))}")

if __name__ == "__main__":
    start()

