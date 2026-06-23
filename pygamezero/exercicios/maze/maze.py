# biblioteca adicional para o comando seguinte
import os

# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# biblioteca pygamezero
import pgzrun
from pygame import Rect
score = 0

# passo do jogador
PASSO = 3
PALT_STATE = True

# define o labirinto
import random


def generate_maze(rows=21, cols=31, coins=13):

    # garante tamanho ímpar
    rows |= 1
    cols |= 1

    maze = [["#" for _ in range(cols)] for _ in range(rows)]

    def carve(r, c):
        maze[r][c] = " "

        dirs = [(0,2),(0,-2),(2,0),(-2,0)]
        random.shuffle(dirs)

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if (
                1 <= nr < rows-1 and
                1 <= nc < cols-1 and
                maze[nr][nc] == "#"
            ):

                maze[r + dr//2][c + dc//2] = " "
                carve(nr, nc)

    # cria caminhos
    carve(1, 1)

    # início
    start = (1, 1)
    maze[start[0]][start[1]] = "S"

    # procura ponto distante
    livres = []

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == " ":
                dist = abs(r-start[0]) + abs(c-start[1])
                livres.append((dist, r, c))

    livres.sort(reverse=True)

    _, gr, gc = livres[0]

    # objetivo
    maze[gr][gc] = "G"

    # moedas
    candidatos = []

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == " ":
                candidatos.append((r, c))

    random.shuffle(candidatos)

    for r, c in candidatos[:coins]:
        maze[r][c] = "C"

    return ["".join(row) for row in maze]


maze = generate_maze(
    rows=21,
    cols=31,
    coins=13
)

# granularidade do labirinto
# cada caracter do labirinto será desenhado VEZES o tamanho da ESCALA
ESCALA = 40

# largura da tela: largura do labirinto VEZES o tamanho da ESCALA
WIDTH = len(maze[0]) * ESCALA

# altura do labirinto: quantidade de elementos no vetor do labirinto (linhas)
# VEZES a ESCALA
HEIGHT = len(maze)* ESCALA
def player_position():
    x = 0
    y = 0
    for row in range(len(maze)):

        # percorrer as colunas do labirinto
            for col in range(len(maze[row])):

            # se for parede...
                if maze[row][col] == "S":
                    x = col*ESCALA
                    y = row*ESCALA
    
    return (x,y)

# jogador: retângulo que começa um pouco depois (5) da posição do labirinto
# o tamanho do jogador é 50 (largura) por 30
x = player_position()
player = Rect(x, (30, 20))

# função que retorna se naquela posição existe ou não parede
def wall_at(x, y):

    # calcula em que posição da matriz o jogador está
    # divide a posição do jogador pela ESCALA,
    # pegando só a parte inteira da divisão
    col = x // ESCALA
    row = y // ESCALA

    # se naquele local houver PARECE, retorna verdadeiro
    # ("colisão": ali tem parede)
    if maze[row][col] == "#":
        return True

    # senão, retorna falso (não tem parede)
    return False

def goal_at(x, y):
    col = x // ESCALA
    row = y // ESCALA

    return maze[row][col] == "G"
def coin_at(x, y):
    col = x // ESCALA
    row = y // ESCALA

    return maze[row][col] == "C"


# função que tenta realizar o movimento
def try_move(dx, dy):

    # verifica se um dos quatro cantos está dentro de alguma parede
    '''
    (x1,y1)    (x2, y1)
    c1 ------ c4
    |          |
    |          |
    c2 ------ c3
    (x1,y2)    (x2,y2)

    '''

    # calcula as posições x1, x2, y1, y2
    x1 = player.x + dx
    x2 = player.x + dx + player.width
    y1 = player.y + dy
    y2 = player.y + dy + player.height
    
    # verifica se os pontos estão "dentro" da parede
    c1 = wall_at(x1, y1)
    c2 = wall_at(x2,y1)
    c3 = wall_at(x2,y2)
    c4 = wall_at(x1,y2)
    
    # se nenhum ponto estiver dentro da parede
    if not (c1 or c2 or c3 or c4):
        # movimenta o jogador
        player.x = x1
        player.y = y1

def update():
    global PALT_STATE, score

    if keyboard.left:
        try_move(-PASSO, 0)

    if keyboard.right:
        try_move(PASSO, 0)

    if keyboard.up:
        try_move(0, -PASSO)

    if keyboard.down:
        try_move(0, PASSO)

    if goal_at(player.centerx, player.centery) and score == 13:
        PALT_STATE = False
    if coin_at(player.centerx, player.centery):

        col = player.centerx // ESCALA
        row = player.centery // ESCALA

        linha = list(maze[row])
        linha[col] = " "

        maze[row] = "".join(linha)

        score += 1

def draw():
    # limpa a tela
    screen.clear()

    if PALT_STATE:
        # percorrer as linhas do labirinto
        for row in range(len(maze)):

        # percorrer as colunas do labirinto
            for col in range(len(maze[row])):

            # se for parede...
                if maze[row][col] == "#":
                # desenha parede :-)
                    wall = Rect(
                        (col * ESCALA, row * ESCALA),
                        (ESCALA, ESCALA)
                    )
                    screen.draw.filled_rect(
                        wall,
                        (100, 100, 100)
                    )
                if maze[row][col] == "G":
                    if score == 13:
                        wall = Rect(
                        (col * ESCALA, row * ESCALA),
                        (ESCALA, ESCALA)
                    )
                        screen.draw.filled_rect(
                        wall,
                        (0, 255, 0)
                    )
                    else:
                        wall = Rect(
                        (col * ESCALA, row * ESCALA),
                        (ESCALA, ESCALA)
                    )
                        screen.draw.filled_rect(
                        wall,
                        (255, 0, 0)
                    )
                if maze[row][col] == "C":
                    wall = Rect(
                        (col * ESCALA + ESCALA / 2.6, row * ESCALA + ESCALA/2.6),
                        (ESCALA/4,ESCALA/4)
                    )
                    screen.draw.filled_rect(
                        wall,
                        (255, 255, 0)
                    )
                screen.draw.text(f"Pontos: {score}",(10,10))
        screen.draw.filled_rect(player, "green")
    else:
        screen.fill((0,100,255))
        screen.draw.text("Você Venceu!!!",(HEIGHT/2, WIDTH/4),color="green", fontsize=80)


# executa o pygme zero
pgzrun.go()

'''
EXERCÍCIOS:
a) mudar a escala do labirinto (valor da variável ESCALA)
b) modificar o labirinto (variável maze)
c) fornecer o labirinto para uma IA e pedir para gerar um labirinto maior

outras melhorias:
https://chatgpt.com/share/6a36f25d-4e18-83e9-a918-1d87a2da7811
'''