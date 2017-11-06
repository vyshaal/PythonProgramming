t = int(input())

while t > 0:
    px,py,qx,qy = map(int,input().split())
    rx = qx + (qx - px)
    ry = qy + (qy - py)
    print(str(rx)+" "+str(ry))
    t -= 1

