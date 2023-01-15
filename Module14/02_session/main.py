# TODO здесь писать код
print("Введите первую точку")
first_coordinate_first_point = float(input('X1: '))
first_coordinate_second_point = float(input('Y1: '))
print("\nВведите вторую точку")
second_coordinate_first_point = float(input('X2: '))
second_coordinate_second_point = float(input('Y2: '))

x_diff = first_coordinate_first_point - second_coordinate_first_point
y_diff = first_coordinate_second_point - second_coordinate_second_point
if x_diff == 0:
    coefficient_k = 1
    coefficient_b = second_coordinate_second_point - coefficient_k * second_coordinate_first_point
    print("Уравнение прямой, проходящей через эти точки будет иметь следующий вид:")
    print("y = ", "x + ", coefficient_b)
else:
    coefficient_k = y_diff / x_diff
    coefficient_b = second_coordinate_second_point - coefficient_k * second_coordinate_first_point
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", coefficient_k, " * x + ", coefficient_b)
