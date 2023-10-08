import random
import secrets
import sys

# параметры по умолчанию
nbits = 8
nms = 1000


# подсчет ранга двоичной матрицы
def gf2_rank(rows):
    rank = 0
    while rows:
        pivot_row = rows.pop()
        if pivot_row:
            rank += 1
            lsb = pivot_row & -pivot_row
            for index, row in enumerate(rows):
                if row & lsb:
                    rows[index] = row ^ pivot_row
    return rank


# генерация случайной матрицы используя random
def random_matrix():
    return [random.getrandbits(nbits) for row in range(nbits)]


# генерация случайной матрицы используя secrets
def random_matrix_s():
    return [secrets.randbits(nbits) for row in range(nbits)]


# генерация нужного количества матриц используя random
def random_matrices(count):
    return [random_matrix() for _ in range(count)]


# генерация нужного количества матриц используя secrets
def random_matrices_s(count):
    return [random_matrix_s() for _ in range(count)]


vec = [0] * nbits


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-n" or sys.argv[1] == "--name":
            nbits = int(sys.argv[2])
            vec = [0] * nbits
        else:
            print(f'Использование:\nrank.py -n <размерность матрицы> -c <количество матриц> [-s]'
                  f'Пример:\nrank.py -n 64 -c 10000\nrank.py -n 8 -c 100000 -s')

        if sys.argv[3] == "-c" or sys.argv[3] == "--count":
            nms = int(sys.argv[4])
        else:
            print(f'Использование:\nrank.py -n <размерность матрицы> -c <количество матриц> [-s]'
                  f'Пример:\nrank.py -n 64 -c 10000\nrank.py -n 8 -c 100000 -s')
        if len(sys.argv) > 5:
            if sys.argv[5] == "-s" or sys.argv[5] == "--secure":
                ms = random_matrices_s(nms)
                for m in ms:
                    vec[gf2_rank(m.copy()) - 1] += 1
        else:
            ms = random_matrices(nms)
            for m in ms:
                vec[gf2_rank(m.copy()) - 1] += 1

    else:
        ms = random_matrices(nms)
        for m in ms:
            vec[gf2_rank(m.copy()) - 1] += 1

print(vec)
