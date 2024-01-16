import cmath


def solve_quad_equation(equation: str = '', a=None, b=None, c=None):
    """
    A function that returns roots of a quadratic equation, including complex
    numbers. Equation must be provided in followed template: ax^2 + bx + c = 0
    or all of 3 coefficients can be given separately using named args.
    """
    if equation:
        operands = []
        if not equation.startswith('-') and not equation.startswith('+'):
            operands.append('+')
        p = 0
        n = equation.index('=')
        while p < n:
            operand = ''
            while equation[p].isdigit():
                operand += equation[p]
                p += 1
            else:
                if equation[p] == '-' or equation[p] == '+':
                    operands.append(equation[p])
                p += 1
            if operand:
                operands.append(operand)
    a = a if a else int(operands[0] + operands[1])
    b = b if b else int(operands[3] + operands[4])
    c = c if c else int(operands[5] + operands[6])
    disc = b ** 2 - 4 * a * c
    return (-b + cmath.sqrt(disc)) / (2 * a), (-b - cmath.sqrt(disc)) / (2 * a)