import argparse

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
    Esta función incrementa el contador global y coloca el valor del contador en las coordenadas especificadas de la matriz.
    """
    global counter
    counter += 1
    for coordinate in coordinates:
        matrix[coordinate[0]][coordinate[1]] = counter

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

    a = b = 0
    matrix[a][b] = -1
    fillRegion(matrixsize, 0, 0)

    for row in matrix:
        print(' '.join(map(lambda x: "{:3}".format(x), row)))

if __name__ == "__main__":
    start()

