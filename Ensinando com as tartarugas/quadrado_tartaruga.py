from turtle import *
#uma função para desenhar uma estrela
#'def' signica 'define'
def quadrado():
    pendown()
    begin_fill()
    for side in range(5):
        left(90)
        forward(50)
    end_fill()
    penup()

#isso vai desenhar uma estrela cinza clara em um fundo azul escuro

color("WhiteSmoke")
bgcolor("MidnightBlue")


#use a função para desenhar estrelas!
quadrado()
forward(100)
quadrado()
left(0)
forward(150)
quadrado()
forward(100)
quadrado()

hideturtle()
done()
