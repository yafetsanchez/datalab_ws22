import math as m

def is_prime(x):
    if (x==1):
        print(f"{x} Este prim")
        return True
    if (x==2):
        print(f"{x} Este prim")
        return True

    if(x%2 == 0):
        print(f"{x} Nu e prim")
        return False

    este_prim = True
    for i in  range(2,x-1):
        if (x%i==0):
            este_prim=False
            break

    if (este_prim):
        print(f"{x} este prim")
    else:
        print(f"{x} Nu este prim")

    return este_prim

if __name__ == "__main__":
    for j in range(100):
        is_prime(j)
