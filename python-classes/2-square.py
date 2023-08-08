class squares:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

Square = __import__('2-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e) 

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)           

my_square_2 = Square(5) 
print("Area: {}".format(my_square_2.area()))   



