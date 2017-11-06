def StairCase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)

StairCase(6)