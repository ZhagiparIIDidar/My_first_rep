class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")

def filter_primes(numbers):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))

# Example usage:
if __name__ == "__main__":
    # Task 1
    sm = StringManipulator()
    sm.getString()
    sm.printString()

    # Task 2
    square = Square(4)
    print(f"Area of square: {square.area()}")

    # Task 3
    rectangle = Rectangle(4, 5)
    print(f"Area of rectangle: {rectangle.area()}")

    # Task 4
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p1.show()
    p2.show()
    print(f"Distance between points: {p1.dist(p2)}")
    p1.move(1, 1)
    p1.show()

    # Task 5
    acc = Account("John", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(150)

    # Task 6
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Prime numbers: {filter_primes(numbers)}")