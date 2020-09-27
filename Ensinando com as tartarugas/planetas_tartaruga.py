from turtle import *
#uma função para desenhar um planeta de um tamanho específico
def drawPlanet(planetSize, planetColour):
    color(planetColour)
    pendown()
    begin_fill()
    for side in range(363):
        left(1)
        forward(planetSize)
    end_fill()
    penup()

#isso desenhar um fundo azul escuro

bgcolor("MidnightBlue")


#use a função para desenhar planeta de tamanhos diferentes!
drawPlanet(1, "Red")
forward(200)
drawPlanet(1.5, "White")
left(120)
forward(0)
drawPlanet(2, "Green")

hideturtle()
done()
