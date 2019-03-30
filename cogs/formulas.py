from math import sqrt

def quad(a, b, c):
    # check no soln
    proto_disc = (b ** 2) - (4 * a * c)
    if proto_disc > 0:
        disc = sqrt((b ** 2) - (4 * a * c))
        x1 = ((-1 * b) + disc) / (2 * a)
        x2 = ((-1 * b) - disc) / (2 * a)
        return(str(x1) + " and " + str(x2))
    elif proto_disc == 0:
        disc = sqrt((b ** 2) - (4 * a * c))
        x1 = ((-1 * b) + disc) / (2 * a)
        return str(x1)
    else:
        return "No solution."

