def percep(x1, x2, w):
    t = 0
    summ = 0

    summ += int(w[2])
    summ += int(x1) * int(w[0])
    summ += int(x2) * int(w[1])

    if (summ >= t):
        y = 1
    elif ((summ >= -t) and (summ <= t)):
        y = 0
    elif (summ < -t):
        y = -1

    return y


def hebb(x1, x2, w):
    outp = int(w[0] / x1) / int(w[1] / x2)
    print(outp)
    return outp
