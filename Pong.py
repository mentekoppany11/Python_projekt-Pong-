import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Pong")
icon_surf = pygame.image.load('C:\\Users\\Koppany\\Desktop\\beadando\\icon.png')
pygame.display.set_icon(icon_surf)

clock = pygame.time.Clock()

font = pygame.font.Font('game_font.ttf')

GRAY       = (128, 128, 128)
LIGHT_GRAY = (64,64,64)
BLUE       = (0, 0, 255)
RED        = (255, 0, 0)
ORANGE     = (255, 165, 0)

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

while True:
    if player1_score != 3 and player2_score != 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.fill(GRAY)

        score_surf = font.render(f'Player1 {player1_score}:{player2_score} Player2', False, LIGHT_GRAY, GRAY)
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
            print(ball_speed_x, ball_speed_y)

        if ball_rect.left >= 1015:
            ball_speed_x = 6
            ball_speed_y = 6
        #Labda sebességének a növelése
            ball_speed_x *= -1.05 #labda irányának a meg fordítása
            ball_speed_y *= 1.05
            print(ball_speed_x, ball_speed_y)
        #Labda visszahelyezése középre
            ball_rect.x = 500
            ball_rect.y = 300
        #Eredmény frissítése
            player1_score += 1
            score_surf = font.render(f'Player1 {player1_score}:{player2_score} Player2', False, LIGHT_GRAY, GRAY)
            score_rect = score_surf.get_rect(midtop = (500, 25))
            screen.blit(score_surf, score_rect)

        if ball_rect.right <= -15:
            ball_speed_x = 6
            ball_speed_y = 6
        #Labda sebességének a növelése
            ball_speed_x *= -1.05 #labda irányának a meg fordítása
            ball_speed_y *= 1.05
            print(ball_speed_x, ball_speed_y)
        #Labda visszahelyezése középre
            ball_rect.x = 500
            ball_rect.y = 300
        #Eredmény frissítése
            player2_score += 1
            score_surf = font.render(f'Player1 {player1_score}:{player2_score} Player2', False, LIGHT_GRAY, GRAY)
            score_rect = score_surf.get_rect(midtop = (500, 25))
            screen.blit(score_surf, score_rect)

        if player1_rect.colliderect(ball_rect) or player2_rect.colliderect(ball_rect):
            ball_speed_x *= -1

        pygame.display.update()
        clock.tick(60)
    else:
        pygame.time.wait(5000)
        break