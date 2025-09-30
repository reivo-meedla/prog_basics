import math


capitalized_name = str.capitalize(input("Please enter your name: "))


if not capitalized_name == "Thanos":
    print(f"Hi, {capitalized_name}. Would you like to have a Hamburger?")
else:
    print("Get out of here, Thanos! Nobody wants to play with you!")


def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: float, c: float) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c ** 2 - a ** 2)
    return b
