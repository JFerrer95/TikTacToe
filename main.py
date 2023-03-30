import pygame
import os
pygame.font.init()
pygame.mixer.init()

# SCREEN INFO
WIDTH, HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tik Tac Toe")
FPS = 60

# COLOR STUFF
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

# GAME BOARD DIMENSIONS
BORDER = pygame.Rect((WIDTH//3 -5), 0, 10, HEIGHT)
BORDER1 = pygame.Rect((WIDTH//3 - 5) * 2 , 0, 10, HEIGHT)
BORDER2 = pygame.Rect(0, (HEIGHT//3) - 5, WIDTH, 10)
BORDER3 = pygame.Rect(0, (HEIGHT//3) * 2 - 5, WIDTH, 10)


# MOVES
FONT = pygame.font.SysFont('comicsans', 100)
global moves
moves = [1,2,3,4,5,6,7,8,9]
global player
player = 'X'

def handle_input(key):
    global player
    global moves
    if (moves[(key - 1)] == 'X' or (moves[key-1] == 'O')):
        print("nah player: " + str(moves[key-1]) + " is already in sqaure: " + str(moves[key]))
        return
    moves[(key - 1)] = player
    draw_move(key)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

def draw_move(square):
    draw_text = FONT.render(player, 1, WHITE)
    if square == 1:
        WIN.blit(draw_text, ((WIDTH/3)/2 - draw_text.get_width()/2, (HEIGHT/3)/2 - draw_text.get_height()/2))
    if square == 2:
        WIN.blit(draw_text, ((WIDTH/3)/2 + (WIDTH/3) - draw_text.get_width()/2, (HEIGHT/3)/2 - draw_text.get_height()/2))
    if square == 3:
        WIN.blit(draw_text, ((WIDTH/3)/2 + (WIDTH/3) + ((WIDTH/3)) - draw_text.get_width()/2, (HEIGHT/3)/2 - draw_text.get_height()/2))
    if square == 4:
        WIN.blit(draw_text, ((WIDTH/3)/2 - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) - draw_text.get_height()/2))
    if square == 5:
        WIN.blit(draw_text, ((WIDTH/3)/2 + (WIDTH/3) - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) - draw_text.get_height()/2))
    if square == 6:
        WIN.blit(draw_text, ((WIDTH/3)/2 + (WIDTH/3) + (WIDTH/3) - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) - draw_text.get_height()/2))
    if square == 7:
        WIN.blit(draw_text, ((WIDTH/3)/2 - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) + (HEIGHT/3) - draw_text.get_height()/2))
    if square == 8:
        WIN.blit(draw_text, ((WIDTH/3)/2 +(WIDTH/3) - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) + (HEIGHT/3) - draw_text.get_height()/2))
    if square == 9:
        WIN.blit(draw_text, ((WIDTH/3)/2 + (WIDTH/3) + (WIDTH/3) - draw_text.get_width()/2, ((HEIGHT/3)/2) + (HEIGHT/3) + (HEIGHT/3) - draw_text.get_height()/2))
    
    pygame.display.update()

    
def key_pressed(event):
    if event.key == (pygame.K_1):
        handle_input(1)
    if event.key == (pygame.K_2):
        handle_input(2)
    if event.key == (pygame.K_3):
        handle_input(3)
    if event.key == (pygame.K_4):
        handle_input(4)
    if event.key == (pygame.K_5):
        handle_input(5)
    if event.key == (pygame.K_6):
        handle_input(6)
    if event.key == (pygame.K_7):
        handle_input(7)
    if event.key == (pygame.K_8):
        handle_input(8)
    if event.key == (pygame.K_9):
        handle_input(9)

def draw_window():
    pygame.display.update()
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, BORDER1)
    pygame.draw.rect(WIN, WHITE, BORDER2)
    pygame.draw.rect(WIN, WHITE, BORDER3)



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                key_pressed(event)

        draw_window()


    main()

    


if __name__ == "__main__":
    main()