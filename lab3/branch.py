import math

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(matrix, i):
    min = maxsize
    for k in range(N):
        if matrix[i][k] < min and i != k:
            min = matrix[i][k]

    return min

def secondMin(matrix, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if matrix[i][j] <= first:
            second = first
            first = matrix[i][j]

        elif(matrix[i][j] <= second and
             matrix[i][j] != first):
            second = matrix[i][j]

    return second


def TSPRec(matrix, curr_bound, curr_weight,
           level, curr_path, visited):
    global final_res

    if level == N:

        if matrix[curr_path[level - 1]][curr_path[0]] != 0:

            curr_res = curr_weight + matrix[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):

        if (matrix[curr_path[level-1]][i] != 0 and visited[i] == False):
            temp = curr_bound
            curr_weight += matrix[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((firstMin(matrix, curr_path[level - 1]) +
                                firstMin(matrix, i)) / 2)
            else:
                curr_bound -= ((secondMin(matrix, curr_path[level - 1]) +
                                firstMin(matrix, i)) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                TSPRec(matrix, curr_bound, curr_weight,
                       level + 1, curr_path, visited)

            curr_weight -= matrix[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(matrix):

    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(matrix, i) +
                       secondMin(matrix, i))

    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TSPRec(matrix, curr_bound, 0, 1, curr_path, visited)


def branchAndBound(matrix):
    global N, maxsize, final_path, final_res
    maxsize = float('inf')
    N = len(matrix)
    final_path = [None] * (N + 1)
    visited = [False] * N
    final_res = maxsize
    TSP(matrix)
    if final_res != maxsize:
        print("Маршрут : ", end=' ')
        for i in range(N + 1):
            print(final_path[i], end=' ')
        print()
        print("Ціна    :", final_res)
        return final_res
    else:
        print("Маршрут не знайдено")
        return 0