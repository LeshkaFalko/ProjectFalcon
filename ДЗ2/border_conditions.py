def border_condition(K):
    # Граничные условия, примененные к глобальной матрице жесткости системы:
    K[0][0] = 1
    for i in range(1, len(K[0])):
        K[0][i] = 0

    for i in range(1, len(K)):
        K[i][0] = 0

    for i in range(0, 3):
        K[3][i] = 0
    for i in range(0, 3):
        K[i][3] = 0
    K[3][3] = 1
    return K
