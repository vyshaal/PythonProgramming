import numpy as np

test_cases = int(input("Enter number of test cases: "))


def calculate(cube,a,b,c,d,e,f):
    sum = 0
    for i in range(a,d+1):
        for j in range(b,e+1):
            for k in range(c,f+1):
                sum += cube[i][j][k]


def execute_case(n,m):
    cube = np.zeros((n,n))
    while m > 0:
        m =- 1
        inp = input()
        if "UPDATE" in inp:
            a,b,c,d,e = inp.split()
            cube[int(b)][int(c)][int(d)] = int(e)
            calculate(cube,1,1,1,n,n,n)
        else:
            a,b,c,d,e,f,g = inp.split()
            calculate(cube,int(b),int(c),int(d),int(e),int(f),int(g))

while test_cases > 0:
    test_cases =- 1
    inp = input("Enter N and M: ")
    n,m = [int(i) for i in inp.split()]
    execute_case(n,m)