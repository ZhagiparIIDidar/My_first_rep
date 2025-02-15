import math

# 1. Программа для преобразования градусов в радианы
def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
radian = degree_to_radian(degree)
print(f"Output radian: {radian:.6f}")

# 2. Программа для вычисления площади трапеции
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area_trapezoid = trapezoid_area(height, base1, base2)
print(f"Expected Output: {area_trapezoid}")

# 3. Программа для вычисления площади правильного многоугольника
def polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area_polygon = polygon_area(num_sides, side_length)
print(f"The area of the polygon is: {area_polygon}")

# 4. Программа для вычисления площади параллелограмма
def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area_parallelogram = parallelogram_area(base, height)
print(f"Expected Output: {area_parallelogram:.1f}")