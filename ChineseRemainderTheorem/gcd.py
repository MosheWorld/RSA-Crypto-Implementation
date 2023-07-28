def gcd(a, b):
    if a == 0:
        gcd_result, x_result, y_result = b, 0, 1
    else:
        gcd_result, x1, y1 = gcd(b % a, a)
        x_result = y1 - (b // a) * x1
        y_result = x1
    return gcd_result, x_result, y_result
