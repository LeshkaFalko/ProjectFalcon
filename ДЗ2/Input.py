# Модуль ввода данных
def get_input():
    EF1 = float(input("введите значения жесткостей элементов: " + "\n" + "EF1 = "))
    EF2 = float(input("EF2 = "))
    EF3 = float(input("EF3 = "))
    C1 = float(input("введите значения жесткостей пружин: " + "\n" + "C1 = "))
    F1 = float(input("введите значение усилия:" + "\n" + "F1 = "))

    return EF1, EF2, EF3, C1, F1
