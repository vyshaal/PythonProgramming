def foundInBermudaTriangle(x1, y1, x2, y2, x3, y3, px, bx, py, by):

    if area(x1, y1, x2, y2, x3, y3) == 0:
        #print("0")
        return 0

    plane_disappear = disappear(px, py, x1, y1, x2, y2, x3, y3)
    boat_disappear = disappear(bx, by, x1, y1, x2, y2, x3, y3)

    if not boat_disappear and plane_disappear:
        #print("1")
        return 1

    if boat_disappear and not plane_disappear:
        #print("2")
        return 2

    if boat_disappear and plane_disappear:
        #print("3")
        return 3

    if not boat_disappear and not plane_disappear:
        #print("4")
        return 4


def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)


def disappear(x,y,x1,y1,x2,y2,x3,y3):
    if area(x1,y1,x2,y2,x3,y3) == area(x,y,x1,y1,x2,y2) + area(x,y,x1,y1,x3,y3) + area(x,y,x2,y2,x3,y3):
        return True
    else:
        return False

#foundInBermudaTriangle(3,1,7,1,5,5,1,2,1,2)