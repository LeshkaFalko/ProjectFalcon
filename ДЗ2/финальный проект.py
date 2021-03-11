

# Вводим начальные данные

from Input import get_input

EF1, EF2, EF3, C1, F1 = get_input()

# Составляем матрицу жесткости
from matrix import matrix

K = matrix(EF1, EF2, EF3, C1)

print("Матрица жескости до введения ГУ" + "\n" + "K:", K)

# Граничные условия
from border_conditions import border_condition

K = border_condition(K)

print("Матрица жескости после введения ГУ" + "\n" + "K:", K)

# Вектор внешних узловых условий:
f = [0, F1, 0, 0, 0]

from matan import inverse_matrix

invK = inverse_matrix(K)

print('обратная', invK)

q = []
for i in range(len(f)):
    u = 0
    for j in range(len(f)):
        u += invK[i][j] * f[j]
    q.append(u)

print('u', q)

# Апроксимации




import first_node_per

first_node_per.per(q[0], q[1])



import second_node_per

second_node_per.per(q[1], q[2])



import third_node_per

third_node_per.per(q[2], q[3])



import first_pr_per

first_pr_per.per(q[4], q[1])






# Внутренние усилия в стержне:
# N = EFu'


import first_node_force

first_node_force.force(q[0], q[1], EF1)



import second_node_force

second_node_force.force(q[1], q[2], EF2)



import third_node_force

third_node_force.force(q[2], q[3], EF3)



import first_pr_force

first_pr_force.force(q[4], q[1], C1)






