def sum_of_digits(P):
    return str(sum([int(i) for i in P]))


def super_digit(P):
    if int(P) < 10:
        return P
    return super_digit(sum_of_digits(P))

n,k = map(int,input().split())

P = ""

P = int(sum_of_digits(str(n)))*k
print(int(super_digit(str(P))))