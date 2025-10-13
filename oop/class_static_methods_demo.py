class Calculator:
    """A simple calculator demonstrating static and class methods."""

    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        This method does not depend on any class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        This method can access class-level data.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b