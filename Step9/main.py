def tribonacci(signature, n):
    j = 2
    for i in range(n-3):
        signature.append(signature[j] + signature[j-1] + signature[j-2])
        j += 1
    return signature[0:n]
