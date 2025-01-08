import pygame
from sys import exit
from time import sleep

pygame.init()

screen = pygame.display.set_mode((1000, 600))

GRAY       = (128, 128, 128)
LIGHT_GRAY = ( 64,  64,  64)
BLUE       = (  0,   0, 255)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)

pygame.display.set_caption("Pong")
try:
    icon_surf = pygame.image.load('icon.png')
    font = pygame.font.Font("game_font.ttf")
except FileNotFoundError as e:
    print(f"Fájl nem található/File not Found: {e}")
    font = pygame.font.Font(None, 30)
    icon_surf = pygame.Surface((32,32))
    icon_surf.fill(RED)


pygame.display.set_icon(icon_surf)

clock = pygame.time.Clock()

player1_surf = pygame.Surface((30, 200))
player1_surf.fill(RED)
player1_rect = player1_surf.get_rect(midleft = (50, 300))

player2_surf = pygame.Surface((30, 200))
player2_surf.fill(BLUE)
player2_rect  = player2_surf.get_rect(midright = (950, 300))

ball_surf = pygame.Surface((20, 20))
ball_surf.fill(ORANGE)
ball_rect = ball_surf.get_rect(center = (500, 300))

ball_speed_x = 6
ball_speed_y = 6

player1_score = 0
player2_score = 0



def countdown(seconds):
    for count in range(seconds, 0, -1):

        screen.fill(GRAY)

        score_surf = font.render(f"Player1 {player1_score}:{player2_score} Player2", False, LIGHT_GRAY, GRAY)
        score_rect = score_surf.get_rect(midtop = (500, 25))
        screen.blit(score_surf, score_rect)

        countdown_surf = font.render(f"Következő kör kezdődik: {count}", False, LIGHT_GRAY, GRAY)
        countdown_rect = countdown_surf.get_rect(center = (500, 300))
        screen.blit(countdown_surf, countdown_rect)

        pygame.display.update()
        sleep(1)

def name_input():

    input_active = True

    input_box_p1 = pygame.Rect(30, 50, 200, 30)
    input_box_p2 = pygame.Rect(770, 50, 200, 30)
    
    input_text_p1 = ""
    input_text_p2 = ""

    active_p1 = False
    active_p2 = False

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_p1.collidepoint(event.pos):
                    active_p1 = not active_p1
                else:
                    active_p1 = False

                if input_box_p2.collidepoint(event.pos):
                    active_p2 = not active_p2
                else:
                    active_p2 = False

            if event.type == pygame.KEYDOWN and len(input_text_p1) <= 14 and active_p1:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text_p1 = input_text_p1[:-1]
                else:
                    input_text_p1 += event.unicode
                    
            if event.type == pygame.KEYDOWN and len(input_text_p2) <= 14 and active_p2:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text_p2 = input_text_p2[:-1]
                else:
                    input_text_p2 += event.unicode

        screen.fill(GRAY)

        player1_name_surf = font.render("PLAYER 1", True, LIGHT_GRAY)
        player1_name_rect = player1_name_surf.get_rect(topleft = (30, 30))
        screen.blit(player1_name_surf, player1_name_rect)

        player2_name_surf = font.render("PLAYER 2", True, LIGHT_GRAY)
        player2_name_rect = player2_name_surf.get_rect(topright = (970, 30))
        screen.blit(player2_name_surf, player2_name_rect)

        pygame.draw.rect(screen, WHITE, input_box_p1)
        pygame.draw.rect(screen, BLACK, input_box_p1, 3)

        pygame.draw.rect(screen, WHITE, input_box_p2)
        pygame.draw.rect(screen, BLACK, input_box_p2, 3)      

        if active_p1:
            pygame.draw.rect(screen, (0, 255, 0), input_box_p1, 3)
            text_surf_p1 = font.render(input_text_p1, True, BLUE)
            screen.blit(text_surf_p1, (input_box_p1.x + 10, input_box_p1.y + 10))
        else:
            pygame.draw.rect(screen, BLACK, input_box_p1, 3)
            text_surf_p1 = font.render(input_text_p1, True, BLUE)
            screen.blit(text_surf_p1, (input_box_p1.x + 10, input_box_p1.y + 10))

        if active_p2:
            pygame.draw.rect(screen, (0, 255, 0), input_box_p2, 3)
            text_surf_p2 = font.render(input_text_p2, True, BLUE)
            screen.blit(text_surf_p2, (input_box_p2.x + 10, input_box_p2.y + 10))
        else:
            pygame.draw.rect(screen, BLACK, input_box_p2, 3)
            text_surf_p2 = font.render(input_text_p2, True, BLUE)
            screen.blit(text_surf_p2, (input_box_p2.x + 10, input_box_p2.y + 10))


        pygame.display.update()
        clock.tick(60)

    return input_text_p1, input_text_p2

player1_name, player2_name = name_input()

while True:
    if player1_score != 3 and player2_score != 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        
        
        screen.fill(GRAY)

        score_surf = font.render(f"{player1_name} {player1_score}:{player2_score} {player2_name}", True, LIGHT_GRAY, GRAY)
        score_rect = score_surf.get_rect(midtop = (500, 25))

        screen.blit(player1_surf, player1_rect)
        screen.blit(player2_surf, player2_rect)

        screen.blit(score_surf, score_rect)

        screen.blit(ball_surf, ball_rect)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and player1_rect.top > 0:
            player1_rect.y -= 5

        if keys[pygame.K_s] and player1_rect.bottom < 600:
            player1_rect.y += 5

        if keys[pygame.K_UP] and player2_rect.top > 0:
            player2_rect.y -= 5

        if keys[pygame.K_DOWN] and player2_rect.bottom < 600:
            player2_rect.y += 5

        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y

        if ball_rect.top <= 0 or ball_rect.bottom >= 600:
            ball_speed_y *= -1.05
            ball_speed_x *= 1.05

        if ball_rect.left >= 1015:
            ball_speed_x = 6
            ball_speed_y = 6
        #Labda sebességének a növelése
            ball_speed_x *= -1.05 #labda irányának a meg fordítása
            ball_speed_y *= 1.05
        #Labda visszahelyezése középre
            ball_rect.x, ball_rect.y= 500, 300
        #Eredmény frissítése
            player1_score += 1
        #Visszaszámláló
            countdown(3)

        if ball_rect.right <= -15:
            ball_speed_x, ball_speed_y = 6, 6
        #Labda sebességének a növelése
            ball_speed_x *= -1.05 #labda irányának a meg fordítása
            ball_speed_y *= 1.05
        #Labda visszahelyezése középre
            ball_rect.x, ball_rect.y= 500, 300
        #Eredmény frissítése
            player2_score += 1
        #Visszaszámláló
            countdown(3)

        if player1_rect.colliderect(ball_rect) or player2_rect.colliderect(ball_rect):
            ball_speed_x *= -1

        pygame.display.update()
        clock.tick(60)
    else:
        pygame.time.wait(5000)
        break