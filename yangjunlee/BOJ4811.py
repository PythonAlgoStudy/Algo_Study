from math import factorial

def catalan(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))


def main():
    while 1:
        n = int(input())
        if n==0:
            break
        print(catalan(n))
    return 0

if __name__ == "__main__":
    main()
