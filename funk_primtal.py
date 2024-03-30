# Funktion til at bestemme om et tal er et primtal

def prim(x):

    if x > 1:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        else:
            return True
    else:
        print("Tallet er negativt!!")

print(prim(11))
print(prim(13))
print(prim(9))
print(prim(-5))