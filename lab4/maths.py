import math

# 1. Программа для преобразования градусов в радианы
def degree_to_radian(degree):
    return degree * (math.pi / 180)

# 2. Программа для вычисления площади трапеции
def trapezoid_area(h, a, b):
    return (a + b) * h / 2

# 3. Программа для вычисления площади правильного многоугольника
def polygon_area(num_sides, len):
    return (num_sides * len ** 2) / (4 * math.tan(math.pi / num_sides))

# 4. Программа для вычисления площади параллелограмма
def parallelogram_area(a, h):
    return a * h


# degree = float(input("Input degree: "))
# print(f"Output radian: {degree_to_radian(degree):.6f}")

# height = float(input("Height: "))
# base1 = float(input("Base, first value: "))
# base2 = float(input("Base, second value: "))
# print(f"Expected Output: {trapezoid_area(height, base1, base2)}")

# num_sides = int(input("Input number of sides: "))
# side_length = float(input("Input the length of a side: "))
# print(f"The area of the polygon is: {polygon_area(num_sides, side_length)}")


# base = float(input("Length of base: "))
# height = float(input("Height of parallelogram: "))
# print(f"Expected Output: {parallelogram_area(base, height):.1f}")