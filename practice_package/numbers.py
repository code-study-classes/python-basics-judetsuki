import math

calculate_distance = lambda x, y: abs(x - y)


calculate_segments = lambda a, b: math.floor(a / b)


calculate_digit_sum = lambda n: sum(map(int, str(abs(n))))


def round_to_multiple(n, m):
    if m == 0:
        return n  
    quotient = n / m
    rounded_quotient = round(quotient)
    return rounded_quotient * m


def calculate_rect_area(x1, x2, y1, y2):
    return abs((x1 - y1) * (x2 - y2))
