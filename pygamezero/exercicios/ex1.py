# biblioteca adicional para o comando seguinte
import os

# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# somente depois do comando acima, 
# importar o módulo pgzrun para rodar o jogo
import pgzrun

# outras bibliotecas auxiliares
from random import randint
import pygame

# definir largura e altura da janela
WIDTH = 1200
HEIGHT = 800

# criar um caçador
quad = Actor('cacador.png')
# definir posição do caçador (x, y)
quad.pos = 300, 200

# velocidade inicial do caçador
quad.vx = 0
quad.vy = 0

# definir a "passada" do caçador
# a quantidade de deslocamentos que o caçador
# vai "andar" a cada movimento
passo_cacador = 1

# definir uma lista de alvos
alvos = []

# cria alguns alvos em posições aleatórias
for i in range(3):
    # criar um novo alvo
    ob = Actor('obstaculo2.png')
    # definir posição aleatória do alvo
    ob.pos = (randint(0, WIDTH), randint(0, HEIGHT))
    # adicionar o alvo na lista
    alvos.append(ob)

# método que vai desenhar as "coisas"
def draw():
    # limpar a tela
    menor_dist = 999999
    indice = 0
    screen.clear()
    # preencher o fundo com a cor verde escuro
    screen.fill((0, 0, 0))
    # desenhar os atores
    quad.draw()
    if alvos:
    # desenhar os alvos
        for i in range(len(alvos)):
            # "pega" o alvo atual
            alvo = alvos[i]
            # desenha o alvo
            alvo.draw()
            dist = ((quad.x - alvos[i].x)**2 + (quad.y - alvos[i].y)**2)**0.5
            if dist < menor_dist:
                menor_dist = dist
                indice = i
            # se for o primeiro alvo...

        screen.draw.circle(alvos[indice].pos, 40, (255, 0, 0))
    screen.draw.text("RAGE:",(0, 4),color="red")
    vida = Rect((65, 3), (passo_cacador*4, 20))
    screen.draw.filled_rect(vida, "red")

# método de atualização da tela
def update():
    global passo_cacador

    # se houver algum alvo
    if alvos:
        menor_dist = 9999
        indice = 0

        for i in range(len(alvos)):
            dist = ((quad.x - alvos[i].x)**2 + (quad.y - alvos[i].y)**2)**0.5

            if dist < menor_dist:
                menor_dist = dist
                indice = i

            alvo = alvos[indice]

        # se o caçador está "longe" do alvo em relação à "X"
        # o que é "longe"? É uma distância maior do que 10
        if abs(quad.x - alvo.x) > 20:
            # interrompe o caçador verticalmente
            # para poder movimentar somente em X
            quad.vy = 0            
            # se o caçador está à direita do alvo...
            if quad.x > alvo.x:
                # ... o caçador vai ter uma velocidade "para a esquerda"
                quad.angle = 180
                quad.vx = - passo_cacador
            else:
                # ... o caçador vai se mover em breve para a direita
                quad.angle = 0
                quad.vx = passo_cacador
        else:
            # interrompe o movimento em X, 
            # pois ele está "alinhado" com o 
            # alvo em "X"
            quad.vx = 0
            # o caçador está abaixo do alvo?
            if quad.y > alvo.y:
                # o caçador vai subir em breve
                quad.angle = 90
                quad.vy = -passo_cacador
            else:
                # o caçador vai descer em breve
                quad.angle = 270
                quad.vy = passo_cacador
            
    # movimentar o ator de acordo com as 
    # velocidades que foram definidas para ele
    else:
        passo_cacador = 1
    quad.x += quad.vx
    quad.y += quad.vy

    # percorre os alvos...
    for alvo in alvos:
        # se o caçador colidiu com algum alvo...
        if quad.colliderect(alvo):
            sounds.gritinho.set_volume(0.5)
            sounds.gritinho.play()
            # remove o alvo da lista
            alvos.remove(alvo)  
            # manda o caçador ficar parado, 
            # pois este poderia ser o último alvo
            # se precisar começar a andar de novo, 
            # ele irá fazer isso, usando a
            # outra lógica de movimentação que está mais acima
            if passo_cacador < 30:
                passo_cacador += 0.2
            quad.vx = 0
            quad.vy = 0 

    # pegar a posição do mouse
    x, y = pygame.mouse.get_pos()
    
    # retornar o estado dos botões (left_click, middle_click, right_click)
    botoes = pygame.mouse.get_pressed()
    
    '''
    # verifica se o botão esquero está apertado
    if botoes[0]: 
        # cria um alvo ali na posição do mouse
        ob = Actor('obstaculo2.png')
        ob.pos = (x,y)
        # adiciona o alvo na lista de alvos
        alvos.append(ob)
    '''
    if randint(0,15) == 0:
            # cria um alvo ali na posição do mouse
        ob = Actor('obstaculo2.png')
        ob.pos = (randint(0, WIDTH), randint(0, HEIGHT))

            # adiciona o alvo na lista de alvos
        alvos.append(ob)
            
# executar o jogo
pgzrun.go()

'''

Ao clicar na tela, novos alvos surgirão na posição do mouse

EXERCÍCIOS:

a) trocar as imagens (por exemplo, pode usar o tema do PacMan)
b) aumentar a velocidade do caçador
c) mudar a busca do caçador: em vez de pegar o "primeiro" alvo da lista, ele
deverá pegar o "último"
d) em vez de pegar o primeiro ou o último alvo da lista, pegar o alvo que estiver mais perto dele :-)

PESQUISE NA internet para descobrir como fazer este exercício abaixo:

e) mudar a imagem do caçador dependendo do lado para o qual ele está indo
'''
