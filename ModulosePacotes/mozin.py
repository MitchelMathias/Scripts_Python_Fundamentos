import turtle as t

t.bgcolor("black")
t.shape('arrow')
t.speed(5)  # Define a velocidade máxima para o desenho


# Função para desenhar o coração
def draw_heart():
    t.penup()
    t.goto(0, -200)  # Move o coração para baixo
    t.pendown()

    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(224)
    t.circle(-112, 200)
    t.left(120)
    t.circle(-112, 200)
    t.forward(224)
    t.end_fill()


# Desenhar o coração
draw_heart()

# Mover para o meio do coração
t.penup()
t.goto(0, -50)  # Ajusta para o texto ficar abaixo do coração
t.pendown()

# Escrever a mensagem
t.color("black")
t.goto(0, -10)
t.write("Mitchel e Larissa", align="center", font=("Times New Roman", 20, "italic"))
t.penup()
t.goto(0, -25)  # Ajusta para o texto ficar abaixo de "Mitchel e Larissa"
t.pendown()
t.write("para", align="center", font=("Times New Roman", 20, "italic"))
t.penup()
t.goto(0, -40)  # Ajusta para o texto ficar abaixo de "para"
t.pendown()
t.write("sempre", align="center", font=("Times New Roman", 20, "italic"))

t.done()

