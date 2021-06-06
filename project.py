print('HI there do you want to draw a shape')
import turtle
lengt=input('pls Input the length of the line you want to draw: ')

if lengt !='':
    length=int(lengt)
else:
    length=100

while length > 0:

    colour=input('pls Input the color of the line you want to draw: ')
    angle=int(input('pls Input the angle of the line you want to draw: '))
    turtle.color(colour)
    turtle.forward(length)
    turtle.right(angle)
    lengt=input('pls Input the length of the line you want to draw: ')

    if lengt !='':
        length=int(lengt)
    else:
        length=100

      
else:
    print('noo')

