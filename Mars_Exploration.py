string = str(input())
dev = 0
while True:
    substring = string[0:3]
    dev += (substring[0] != 'S') + (substring[1] != 'O') + (substring[2] != 'S')
    string = string[3:]
    if len(string) == 0:
        break
print(dev)