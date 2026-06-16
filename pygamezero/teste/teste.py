# importar o módulo pgzrun para rodar o jogo
import os
# Esta linha força o sistema operacional a centralizar a janela do jogo
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

import pgzrun

# criar um "ator"
quad = Actor('quadrado.png')

# definir posição do ator (x, y)
quad.pos = 300, 1

quad2 = Actor('quadrado2.png')

quad2.pos = 450, -200
velquad1 = 0
velquad2 = 0

# criar uma "base"
base = Actor('base.png')


base.width = 1000
base.height = 1000
# definir a posição da base
base.pos = 400, 600
i=100
i2=100

# definir largura e altura da janela
TITLE = "YURI ALBERTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
WIDTH = 800
HEIGHT = 600

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.fill((150,200,255))
    # desenhar os atores
    quad.draw()
    quad2.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():
    global i
    global i2
    global velquad1
    global velquad2
    
    # se o ator NÃO colidiu com a base...
    if not quad.colliderect(base):
        # o ator continua "caindo"
        velquad1 += 1
        quad.top += velquad1
    else:
        velquad1 = 0
        quad.top -= i
        if i > 0:
            i = i - 10
    if not quad2.colliderect(base):
        # o ator continua "caindo"
        velquad2 += 1
        quad2.top += velquad2
    else:
        velquad2 = 0
        quad2.top -= i2
        if i2 > 0:
            i2 = i2 - 10
    if quad.top > 600 or quad.top < 0:
        exit()

# executar o jogo
pgzrun.go()

''' EXERCÍCIOS:

a) aumentar a velocidade de queda do quadrado
b) mudar a posição inicial do quadrado (colocar o quadrado mais alto)
c) mudar a posição da base (colocar a base mais para baixo)
d) mudar as figuras da base e do quadrado
e) colocar 2 quadrados caindo ao mesmo tempo

Para fazer as atividades a seguir, você deverá buscar na Internet/IA
como realizá-las no pygame zero:

f) alterar a cor de fundo da janela
===> "como alterar a cor de fundo da janela no pygame zero"
g) centralizar a janela na tela
===> "como centralizar a janela no pygame zero"
h) colocar um título na janela
===> "como colocar um título na janela no pygame zero"

'''