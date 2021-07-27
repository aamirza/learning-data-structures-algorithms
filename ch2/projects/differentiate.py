"""Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative
of that polynomial."""

import re

def differentiate(polynomial):
    """The polynomial must be of the format ax^m + bx^n + cx + d and be separated by spaces."""
    polynomial_pattern = re.compile(r'(\-|\+)?\s?(\d*)(x?)\^?(\d)*\s?')
    expressions = polynomial_pattern.findall(polynomial)
    if expressions[-1] == ('', '', ''): expressions.pop(-1)  # It might give an empty expression at the end.

    derivative = ''
    for nomial in expressions:
        sign = '+' if nomial[0] in ('+', '') else '-'
        coefficient = nomial[1] if nomial[1] != '' else '1'
        has_x = nomial[2] == 'x'
        if not has_x:
            exponent = 0
        else:
            exponent = int(nomial[3]) if nomial[3] != '' else 1


        # derivative
        new_coefficient = int(sign + coefficient) * int(exponent)
        exponent -= 1
        if new_coefficient == 0:
            # It is now zero, so nothing to add to the expression
            pass
        else:
            derivative += f"{sign if not (derivative == '' and sign == '+') else ''}" \
                          f"{'' if derivative == '' else ' '}" \
                          f"{'' if coefficient == 1 and exponent >= 1 else abs(new_coefficient)}" \
                          f"{'x' if exponent >= 1 else ''}" \
                          f"{f'^{exponent}' if exponent > 1 and has_x else ''}" \
                          f" "
    return derivative.rstrip()  # remove trailing whitespace


if __name__ == "__main__":
    assert differentiate("2x^2 + 5x - 4") == "4x + 5"
    assert differentiate("-18x^9 + 7x^4 - x^3 + x - 19") == "-162x^8 + 28x^3 - 3x^2 + 1"
