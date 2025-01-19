from robot.api.deco import keyword

class MathOperation:

    @keyword
    def add_numbers(self, a, b):
        # Parse inputs to integers before performing addition
        a = int(a)
        b = int(b)
        return a + b

    @keyword
    def multiply_numbers(self, a, b):
        # Parse inputs to integers before performing multiplication
        a = int(a)
        b = int(b)
        return a * b
