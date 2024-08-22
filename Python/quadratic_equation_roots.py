import math


def find_roots(a, b, c):
    # Format the quadratic equation
    equation = f"{a}x^2"
    if b < 0:
        equation += f" - {-b}x"
    else:
        equation += f" + {b}x"
    if c < 0:
        equation += f" - {-c}"
    else:
        equation += f" + {c}"

    equation += " = 0"

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if discriminant is positive, zero or negative
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The equation {equation} has two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return f"The equation {equation} has one real root: {root}"
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"The equation {equation} has complex roots: {real_part} ± {imaginary_part}i"


# Example usage:
a = 1
b = -7
c = 10

result = find_roots(a, b, c)
print(result)
