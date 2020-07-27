import turtle

def sarena_duz(n, a, boja1, boja2):
    for i in range(n):
        if i % 2 == 0:
            turtle.color(boja1)
        else:
            turtle.color(boja2)
        turtle.forward(a)


turtle.width(10)
sarena_duz(11, 10, "red", "blue")
turtle.left(90)
sarena_duz(11, 10, "green", "yellow")
turtle.left(90)
sarena_duz(11, 10, "orange", "black")
turtle.left(90)
sarena_duz(11, 10, "purple", "cyan")
turtle.left(90)

            
