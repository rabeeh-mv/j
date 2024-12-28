from turtle import*
pensize(3)
color("black","green")
for r in range(4):
    rt(90)
    begin_fill()
    for i in range(40,101,20):
        circle(i)
    end_fill()
   
