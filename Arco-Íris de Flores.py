import turtle
t = turtle.Pen()
t.speed(0)
t.up()
t.goto(-500,-250)
t.down()
colors = ['red' , 'orange' , 'yellow' , 'lime' , 'blue' , 'indigo' , 'violet']
for i in range(5):
    j = i*10
    for i in range(10):
        k = (i+j) % 7
        t.fillcolor(colors[k])
        t.begin_fill()
        for i in range(12):
            for i in range(3):
                t.circle(10, 360, 6)
                t.left(120)
            t.left(30)
            t.forward(10)
        t.end_fill()
        t.up()
        t.forward(100)
        t.down()
    t.up()
    t.back(1000)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.down()

turtle.done()












