def linear_equation(k, b):
    if (k == 0 and b != 0) or (b == 0 and k == 0):
        return 'None'
    else:
        x = (- b)/k
        return x