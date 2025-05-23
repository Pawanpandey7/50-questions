# power of the number using recursion
def pow(n,p):
    if p == 1:
        return n

    elif p == 0:
        return 1

    else :
        return n * pow(n,p-1)


print(pow(2,3))

