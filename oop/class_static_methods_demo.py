# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances of the class
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        It does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        It has access to the class itself (cls) and can use class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")
