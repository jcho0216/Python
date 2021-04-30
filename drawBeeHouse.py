import turtle
t = turtle.Turtle()
t.shape('turtle')

def line(): 
    t.forward(80)
    t.left(60)

def hex():
    line()
    line()
    line()
    line()
    line()
    line()
  

def hive():
    hex()
    t.forward(80)
    t.right(60)

hive(), hive(), hive(), hive(), hive(), hive()