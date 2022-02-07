def square_digits(num):
    res = ""
    for i in range(len(str(num))):
        res = res + str(int(str(num)[i]) ** 2)
    return int(res)
