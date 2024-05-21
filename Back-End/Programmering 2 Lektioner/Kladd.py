import turtle
var = turtle.Turtle()

# Rita en blomma
for _ in range(36):
    var.circle(50)    # Rita en cirkel med radien 50
    var.right(10)     # Sväng höger 10 grader

# Avsluta ritningen
turtle.done()