from turtle import*

#draw pentagons inside each other

#set number of shapes
number_of_shapes = 4

#set length of side
length_of_side = 20

#draws pentagon
for shape in range(number_of_shapes):
    for side in range(5):
        forward(length_of_side)
        left(72)
#move to the next position
    penup()
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(180)
    pendown()
    length_of_side += 20
    
