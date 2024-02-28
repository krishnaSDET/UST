def swaping(xa, xy):
    global x, y
    x, y = xy, xa

if __name__== '__main__':

    x= input("enter the number ")
    y= input("enter the number ")
    swaping(x,y)
    print(f'the values of {x} and {y}')