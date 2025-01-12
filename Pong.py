import pygame
from random import choice
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((1000, 600))

GRAY       = (128, 128, 128)
RED        = (255,   0,   0)
DARK_GREEN = (  0, 120,   0)
BLUE       = (  0,   0, 255)
YELLOW     = (255, 255,   0)
PURPLE     = (150,   0, 255)
LIGHT_GRAY = ( 64,  64,  64)
ORANGE     = (255, 165,   0)
GREEN      = (  0, 255,   0)
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)

pygame.display.set_caption("Pong")
try:
    icon_surf = pygame.image.load("icon.png").convert_alpha()
    font = pygame.font.Font("game_font.ttf")
except FileNotFoundError as e:
    print(f"Fájl nem található/File not Found: {e}")
    font = pygame.font.Font(None, 30)
    icon_surf = pygame.Surface((32,32))
    icon_surf.fill(RED)

pygame.display.set_icon(icon_surf)

clock = pygame.time.Clock()

ball_surf = pygame.image.load('ball.png').convert_alpha()
ball_rect = ball_surf.get_rect(center = (500, 300))

ball_speed_x = choice([5, -5])
ball_speed_y = choice([5, -5])
max_speed = 10

player1_score = 0
player2_score = 0

def home():

    multiplayer_box = pygame.Rect(400, 260, 200, 40)
    multiplayer_surf = font.render("2 PLAYER MODE", True, BLACK)
    multiplayer_rect = multiplayer_surf.get_rect(center = (500, 280))
    multiplayer_draw = pygame.draw.rect(screen, WHITE, multiplayer_box)
    multiplayer_draw_hover = False
    multiplayer_active = False

    solo_box = pygame.Rect(400, 310, 200, 40)
    solo_surf = font.render("1 PLAYER MODE", True, BLACK)
    solo_rect = solo_surf.get_rect(center = (500, 330))
    solo_draw = pygame.draw.rect(screen, WHITE, solo_box)
    solo_draw_hover = False
    solo_active = False

    binds_box = pygame.Rect(400, 360, 200, 40)
    binds_surf = font.render("OPTIONS", True, BLACK)
    binds_rect = binds_surf.get_rect(center = (500, 380))
    binds_draw = pygame.draw.rect(screen, WHITE, binds_box)
    binds_draw_hover = False

    title_font = pygame.font.Font("game_font.ttf", 35)
    title_surf = title_font.render("PONG ARCADE GAME",True, BLACK)
    title_rect = title_surf.get_rect(center = (500, 100))

    while solo_active == False and multiplayer_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEMOTION:
                if multiplayer_draw.collidepoint(event.pos) or multiplayer_rect.collidepoint(event.pos):
                    multiplayer_draw_hover = True
                else:
                    multiplayer_draw_hover = False
                
                if solo_draw.collidepoint(event.pos) or solo_rect.collidepoint(event.pos):
                    solo_draw_hover = True
                else:
                    solo_draw_hover = False

                if binds_draw.collidepoint(event.pos) or binds_rect.collidepoint(event.pos):
                    binds_draw_hover = True
                else:
                    binds_draw_hover = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if multiplayer_draw.collidepoint(event.pos) or multiplayer_rect.collidepoint(event.pos):
                    multiplayer_active = True

                if solo_draw.collidepoint(event.pos) or solo_rect.collidepoint(event.pos):
                    solo_active = True

        screen.fill(GRAY)

        screen.blit(title_surf, title_rect)

        pygame.draw.rect(screen, WHITE, multiplayer_box)
        pygame.draw.rect(screen, BLACK, multiplayer_box, 3)
        screen.blit(multiplayer_surf, multiplayer_rect)

        pygame.draw.rect(screen, WHITE, solo_box)
        pygame.draw.rect(screen, BLACK, solo_box, 3)
        screen.blit(solo_surf, solo_rect)

        pygame.draw.rect(screen, WHITE, binds_box)
        pygame.draw.rect(screen, BLACK, binds_box, 3)
        screen.blit(binds_surf, binds_rect)

        if multiplayer_draw_hover:
            pygame.draw.rect(screen, GREEN, multiplayer_box, 3)
        
        if solo_draw_hover:
            pygame.draw.rect(screen, GREEN, solo_box, 3)
        
        if binds_draw_hover:
            pygame.draw.rect(screen, GREEN, binds_box, 3)

        pygame.display.update()
        clock.tick(60)

    return solo_active

def countdown(seconds):

    countdown_font = pygame.font.Font("game_font.ttf", 70)

    for count in range(seconds, 0, -1):

        screen.fill(GRAY)

        countdown_surf = countdown_font.render(str(count), True, BLACK)
        countdown_rect = countdown_surf.get_rect(center = (500, 300))
        screen.blit(countdown_surf, countdown_rect)

        pygame.display.update()
        time.sleep(1)

    screen.fill(GRAY)

    countdown_surf = countdown_font.render("GO", True, BLACK)
    countdown_rect = countdown_surf.get_rect(center = (500, 300))
    screen.blit(countdown_surf, countdown_rect)

    pygame.display.update()
    time.sleep(1)

def name_input():

    active = True

    input_box_p1 = pygame.Rect(30, 50, 200, 30)
    input_box_p2 = pygame.Rect(770, 50, 200, 30)

    submit_box = pygame.Rect(425, 510, 150, 40)
    submit_box_hover = False
    
    input_text_p1 = ""
    input_text_p2 = ""

    active_p1 = False
    active_p2 = False

    submit_surf = font.render("SUBMIT", True, BLACK)
    submit_rect = submit_surf.get_rect(center = (500, 530))
    submit_draw = pygame.draw.rect(screen, DARK_GREEN, submit_box)

    player1_name_surf = font.render("PLAYER 1", True, BLACK)
    player1_name_rect = player1_name_surf.get_rect(topleft = (30, 30))

    player2_name_surf = font.render("PLAYER 2", True, BLACK)
    player2_name_rect = player2_name_surf.get_rect(topright = (970, 30))

    color_p1 = 'paddle_red.png'
    color_p2 = 'paddle_blue.png'
    name_color_p1 = RED
    name_color_p2 = BLUE

    color_box_red_p1 = pygame.Rect(input_box_p1.left, input_box_p1.bottom + 10, 32, 32)
    color_box_red_active_p1 = True

    color_box_red_p2 = pygame.Rect(input_box_p2.left, input_box_p1.bottom + 10, 32, 32)
    color_box_red_active_p2 = False

    color_box_blue_p1 = pygame.Rect(input_box_p1.left + 42, input_box_p1.bottom + 10, 32, 32)
    color_box_blue_active_p1 = False

    color_box_blue_p2 = pygame.Rect(input_box_p2.left + 42, input_box_p1.bottom + 10, 32, 32)
    color_box_blue_active_p2 = True

    color_box_green_p1 = pygame.Rect(input_box_p1.left + 84, input_box_p1.bottom + 10, 32, 32)
    color_box_green_active_p1 = False

    color_box_green_p2 = pygame.Rect(input_box_p2.left + 84, input_box_p1.bottom + 10, 32, 32)
    color_box_green_active_p2 = False

    color_box_yellow_p1 = pygame.Rect(input_box_p1.left + 126, input_box_p1.bottom + 10, 32, 32)
    color_box_yellow_active_p1 = False

    color_box_yellow_p2 = pygame.Rect(input_box_p2.left + 126, input_box_p1.bottom + 10, 32, 32)
    color_box_yellow_active_p2 = False

    color_box_purple_p1 = pygame.Rect(input_box_p1.left + 168, input_box_p1.bottom + 10, 32, 32)
    color_box_purple_active_p1 = False

    color_box_purple_p2 = pygame.Rect(input_box_p2.left + 168, input_box_p1.bottom + 10, 32, 32)
    color_box_purple_active_p2 = False

    while active:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_p1.collidepoint(event.pos):
                    active_p1 = not active_p1
                    active_p2 = False

                if input_box_p2.collidepoint(event.pos):
                    active_p2 = not active_p2
                    active_p1 = False

                if color_box_red_p1.collidepoint(event.pos):
                    color_p1 = 'paddle_red.png'
                    name_color_p1 = RED
                elif color_box_blue_p1.collidepoint(event.pos):
                    color_p1 = 'paddle_blue.png'
                    name_color_p1 = BLUE
                elif color_box_green_p1.collidepoint(event.pos):
                    color_p1 = 'paddle_green.png'
                    name_color_p1 = DARK_GREEN
                elif color_box_yellow_p1.collidepoint(event.pos):
                    color_p1 = 'paddle_yellow.png'
                    name_color_p1 = YELLOW
                elif color_box_purple_p1.collidepoint(event.pos):
                    color_p1 = 'paddle_purple.png'
                    name_color_p1 = PURPLE

                if color_box_red_p2.collidepoint(event.pos):
                    color_p2 = 'paddle_red.png'
                    name_color_p2 = RED
                elif color_box_blue_p2.collidepoint(event.pos):
                    color_p2 = 'paddle_blue.png'
                    name_color_p2 = BLUE
                elif color_box_green_p2.collidepoint(event.pos):
                    color_p2 = 'paddle_green.png'
                    name_color_p2 = GREEN
                elif color_box_yellow_p2.collidepoint(event.pos):
                    color_p2 = 'paddle_yellow.png'
                    name_color_p2 = YELLOW
                elif color_box_purple_p2.collidepoint(event.pos):
                    color_p2 = 'paddle_purple.png'
                    name_color_p2 = PURPLE

                if color_box_red_p1.collidepoint(event.pos):
                    color_box_red_active_p1 = not color_box_red_active_p1
                    color_box_green_active_p1 = False
                    color_box_blue_active_p1 = False
                    color_box_yellow_active_p1 = False
                    color_box_purple_active_p1 = False

                if color_box_green_p1.collidepoint(event.pos):
                    color_box_green_active_p1 = not color_box_green_active_p1
                    color_box_red_active_p1 = False
                    color_box_blue_active_p1 = False
                    color_box_yellow_active_p1 = False
                    color_box_purple_active_p1 = False

                if color_box_blue_p1.collidepoint(event.pos):
                    color_box_blue_active_p1 = not color_box_blue_active_p1
                    color_box_red_active_p1 = False
                    color_box_green_active_p1 = False
                    color_box_yellow_active_p1 = False
                    color_box_purple_active_p1 = False

                if color_box_yellow_p1.collidepoint(event.pos):
                    color_box_yellow_active_p1 = not color_box_yellow_active_p1
                    color_box_red_active_p1 = False
                    color_box_green_active_p1 = False
                    color_box_blue_active_p1 = False
                    color_box_purple_active_p1 = False

                if color_box_purple_p1.collidepoint(event.pos):
                    color_box_purple_active_p1 = not color_box_purple_active_p1
                    color_box_red_active_p1 = False
                    color_box_green_active_p1 = False
                    color_box_blue_active_p1 = False
                    color_box_yellow_active_p1 = False

                if color_box_red_p2.collidepoint(event.pos):
                    color_box_red_active_p2 = not color_box_red_active_p2
                    color_box_green_active_p2 = False
                    color_box_blue_active_p2 = False
                    color_box_purple_active_p2 = False
                    color_box_yellow_active_p2 = False

                if color_box_green_p2.collidepoint(event.pos):
                    color_box_green_active_p2 = not color_box_green_active_p2
                    color_box_red_active_p2 = False
                    color_box_blue_active_p2 = False
                    color_box_purple_active_p2 = False
                    color_box_yellow_active_p2 = False

                if color_box_blue_p2.collidepoint(event.pos):
                    color_box_blue_active_p2 = not color_box_blue_active_p2
                    color_box_red_active_p2 = False
                    color_box_green_active_p2 = False
                    color_box_purple_active_p2 = False
                    color_box_yellow_active_p2 = False

                if color_box_yellow_p2.collidepoint(event.pos):
                    color_box_yellow_active_p2 = not color_box_yellow_active_p2
                    color_box_red_active_p2 = False
                    color_box_green_active_p2 = False
                    color_box_blue_active_p2 = False
                    color_box_purple_active_p2 = False

                if color_box_purple_p2.collidepoint(event.pos):
                    color_box_purple_active_p2 = not color_box_purple_active_p2
                    color_box_red_active_p2 = False
                    color_box_green_active_p2 = False
                    color_box_blue_active_p2 = False
                    color_box_yellow_active_p2 = False

                if submit_draw.collidepoint(event.pos) or submit_rect.collidepoint(event.pos):
                    active = False

            if event.type == pygame.KEYDOWN and len(input_text_p1) <= 14 and active_p1:
                if event.key == pygame.K_BACKSPACE:
                    input_text_p1 = input_text_p1[:-1]
                else:
                    input_text_p1 += event.unicode
                    
            if event.type == pygame.KEYDOWN and len(input_text_p2) <= 14 and active_p2:
                if event.key == pygame.K_BACKSPACE:
                    input_text_p2 = input_text_p2[:-1]
                else:
                    input_text_p2 += event.unicode
            
            if event.type == pygame.MOUSEMOTION:
                if submit_draw.collidepoint(event.pos) or submit_rect.collidepoint(event.pos):
                    submit_box_hover = True
                else:
                    submit_box_hover = False 

        screen.fill(GRAY)

        screen.blit(player2_name_surf, player2_name_rect)
        screen.blit(player1_name_surf, player1_name_rect)

        pygame.draw.rect(screen, WHITE, input_box_p1)
        pygame.draw.rect(screen, BLACK, input_box_p1, 3)

        pygame.draw.rect(screen, RED, color_box_red_p1)
        pygame.draw.rect(screen, BLACK, color_box_red_p1, 3)

        pygame.draw.rect(screen, DARK_GREEN, color_box_green_p1)
        pygame.draw.rect(screen, BLACK, color_box_green_p1, 3)

        pygame.draw.rect(screen, BLUE, color_box_blue_p1)
        pygame.draw.rect(screen, BLACK, color_box_blue_p1, 3)

        pygame.draw.rect(screen, YELLOW, color_box_yellow_p1)
        pygame.draw.rect(screen, BLACK, color_box_yellow_p1, 3)

        pygame.draw.rect(screen, PURPLE, color_box_purple_p1)
        pygame.draw.rect(screen, BLACK, color_box_purple_p1, 3)

        pygame.draw.rect(screen, RED, color_box_red_p2)
        pygame.draw.rect(screen, BLACK, color_box_red_p2, 3)

        pygame.draw.rect(screen, DARK_GREEN, color_box_green_p2)
        pygame.draw.rect(screen, BLACK, color_box_green_p2, 3)

        pygame.draw.rect(screen, BLUE, color_box_blue_p2)
        pygame.draw.rect(screen, BLACK, color_box_blue_p2, 3)

        pygame.draw.rect(screen, YELLOW, color_box_yellow_p2)
        pygame.draw.rect(screen, BLACK, color_box_yellow_p2, 3)

        pygame.draw.rect(screen, PURPLE, color_box_purple_p2)
        pygame.draw.rect(screen, BLACK, color_box_purple_p2, 3)

        pygame.draw.rect(screen, WHITE, input_box_p2)
        pygame.draw.rect(screen, BLACK, input_box_p2, 3)  
        
        pygame.draw.rect(screen, DARK_GREEN, submit_box)
        pygame.draw.rect(screen, BLACK, submit_box, 3)

        screen.blit(submit_surf, submit_rect)

        if active_p1:
            pygame.draw.rect(screen, GREEN, input_box_p1, 3)
            text_surf_p1 = font.render(input_text_p1, True, BLUE)
            screen.blit(text_surf_p1, (input_box_p1.x + 10, input_box_p1.y + 10))
        else:
            pygame.draw.rect(screen, BLACK, input_box_p1, 3)
            text_surf_p1 = font.render(input_text_p1, True, BLUE)
            screen.blit(text_surf_p1, (input_box_p1.x + 10, input_box_p1.y + 10))

        if active_p2:
            pygame.draw.rect(screen, GREEN, input_box_p2, 3)
            text_surf_p2 = font.render(input_text_p2, True, BLUE)
            screen.blit(text_surf_p2, (input_box_p2.x + 10, input_box_p2.y + 10))
        else:
            pygame.draw.rect(screen, BLACK, input_box_p2, 3)
            text_surf_p2 = font.render(input_text_p2, True, BLUE)
            screen.blit(text_surf_p2, (input_box_p2.x + 10, input_box_p2.y + 10))
        
        if submit_box_hover:
            pygame.draw.rect(screen, GREEN, submit_box)
            pygame.draw.rect(screen, BLACK, submit_box, 3)
            screen.blit(submit_surf, submit_rect)

        if color_box_red_active_p1:
            pygame.draw.rect(screen, RED, color_box_red_p1)
            pygame.draw.rect(screen, GREEN, color_box_red_p1, 3)
        
        if color_box_red_active_p2:
            pygame.draw.rect(screen, RED, color_box_red_p2)
            pygame.draw.rect(screen, GREEN, color_box_red_p2, 3)

        if color_box_green_active_p1:
            pygame.draw.rect(screen, DARK_GREEN, color_box_green_p1)
            pygame.draw.rect(screen, GREEN, color_box_green_p1, 3)

        if color_box_green_active_p2:
            pygame.draw.rect(screen, DARK_GREEN, color_box_green_p2)
            pygame.draw.rect(screen, GREEN, color_box_green_p2, 3)

        if color_box_blue_active_p1:
            pygame.draw.rect(screen, BLUE, color_box_blue_p1)
            pygame.draw.rect(screen, GREEN, color_box_blue_p1, 3)

        if color_box_blue_active_p2:
            pygame.draw.rect(screen, BLUE, color_box_blue_p2)
            pygame.draw.rect(screen, GREEN, color_box_blue_p2, 3)

        if color_box_yellow_active_p1:
            pygame.draw.rect(screen, YELLOW, color_box_yellow_p1)
            pygame.draw.rect(screen, GREEN, color_box_yellow_p1, 3)

        if color_box_yellow_active_p2:
            pygame.draw.rect(screen, YELLOW, color_box_yellow_p2)
            pygame.draw.rect(screen, GREEN, color_box_yellow_p2, 3)

        if color_box_purple_active_p1:
            pygame.draw.rect(screen, PURPLE, color_box_purple_p1)
            pygame.draw.rect(screen, GREEN, color_box_purple_p1, 3)

        if color_box_purple_active_p2:
            pygame.draw.rect(screen, PURPLE, color_box_purple_p2)
            pygame.draw.rect(screen, GREEN, color_box_purple_p2, 3)

        pygame.display.update()
        clock.tick(60)

    if input_text_p1 == "":
        input_text_p1 = "PLAYER1"

    if input_text_p2 == "":
        input_text_p2 = "PLAYER2"

    return input_text_p1, input_text_p2, color_p1, color_p2, name_color_p1, name_color_p2

game_mode = home()

player1_name, player2_name, color_p1, color_p2, name_color_p1, name_color_p2 = name_input()

player1_surf = pygame.image.load(color_p1).convert_alpha()
player1_rect = player1_surf.get_rect(midleft = (50, 300))
player1_name_surf = font.render(f"{player1_name}", True, name_color_p1)
player1_name_rect = player1_name_surf.get_rect(topleft = (100, 25))

player2_surf = pygame.image.load(color_p2).convert_alpha()
player2_rect  = player2_surf.get_rect(midright = (950, 300))
player2_name_surf = font.render(f"{player2_name}", True, name_color_p2)
player2_name_rect = player2_name_surf.get_rect(topright = (900, 25))

replay_box = pygame.Rect(345, 510, 150, 40)
replay_box_hover = False

replay_surf = font.render("REPLAY", True, BLACK)
replay_rect = replay_surf.get_rect(center = (420, 530))
replay_draw = pygame.draw.rect(screen, DARK_GREEN, replay_box)
replay = False

end_box = pygame.Rect(505, 510, 150, 40)
end_box_hover = False

end_surf = font.render("QUIT GAME", True, BLACK)
end_rect = end_surf.get_rect(center = (580, 530))
end_draw = pygame.draw.rect(screen, DARK_GREEN, end_box)
end = True


countdown(3)

while end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            if replay_draw.collidepoint(event.pos) or replay_rect.collidepoint(event.pos):
                replay_box_hover = True
            else:
                replay_box_hover = False

            if end_draw.collidepoint(event.pos) or end_rect.collidepoint(event.pos):
                end_box_hover = True
            else:
                end_box_hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if replay_draw.collidepoint(event.pos) or replay_rect.collidepoint(event.pos):
                replay = True

            if end_draw.collidepoint(event.pos) or end_rect.collidepoint(event.pos):
                end = False

    if replay:
        player1_score = 0
        player2_score = 0
        ball_speed_x = choice([5, -5])
        ball_speed_y = choice([5, -5])
        ball_rect.x = 500
        ball_rect.y = 300
        player1_rect.x = 30
        player1_rect.y = 200
        player2_rect.x = 900
        player2_rect.y = 200
        replay = False
        countdown(3)

    if player1_score < 3 and player2_score < 3:

        if game_mode:
            if ball_rect.centery > player2_rect.centery and player2_rect.centery < 500:
                player2_rect.y += 5
            elif ball_rect.centery < player2_rect.centery and player2_rect.centery > 100:
                player2_rect.y -= 5

        screen.fill(GRAY)

        

        score_surf = font.render(f"{player1_score}:{player2_score}", True, BLACK)
        score_rect = score_surf.get_rect(midtop = (500, 25))

        screen.blit(player1_surf, player1_rect)
        screen.blit(player2_surf, player2_rect)

        screen.blit(score_surf, score_rect)

        screen.blit(player1_name_surf, player1_name_rect)
        screen.blit(player2_name_surf, player2_name_rect)

        screen.blit(ball_surf, ball_rect)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and player1_rect.centery > 100:
            player1_rect.y -= 5

        if keys[pygame.K_s] and player1_rect.centery < 500:
            player1_rect.y += 5

        if keys[pygame.K_UP] and player2_rect.centery > 100 and game_mode == False:
            player2_rect.y -= 5

        if keys[pygame.K_DOWN] and player2_rect.centery < 500 and game_mode == False:
            player2_rect.y += 5

        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y

        if ball_rect.top <= 0 or ball_rect.bottom >= 600:
            ball_speed_x = max(min(ball_speed_x *  1.01, max_speed), - max_speed)
            ball_speed_y = max(min(ball_speed_y * -1.01, max_speed), - max_speed)

        if ball_rect.left >= 1000:
            ball_speed_x = choice([5, -5])
            ball_speed_y = choice([5, -5])
            ball_rect.x = 500
            ball_rect.y = 300
            player1_rect.x = 50
            player1_rect.y = 200
            player2_rect.x = 920
            player2_rect.y = 200
            player1_score += 1
            if player1_score != 3:
                countdown(3)

        if ball_rect.right <= 0:
            ball_speed_x = choice([5, -5])
            ball_speed_y = choice([5, -5])
            ball_rect.x = 500
            ball_rect.y = 300
            player1_rect.x = 50
            player1_rect.y = 200
            player2_rect.x = 920
            player2_rect.y = 200
            player2_score += 1
            if player2_score != 3:
                countdown(3)
        
        if player1_rect.collidepoint(ball_rect.midleft) or player2_rect.collidepoint(ball_rect.midright):
                ball_speed_x = max(min(ball_speed_x * -1.01, max_speed), -max_speed)
                ball_speed_y = max(min(ball_speed_y * 1.01, max_speed), -max_speed)

        pygame.display.update()
        clock.tick(60)

    elif player1_score == 3 or player2_score == 3:

        winner_font = pygame.font.Font("game_font.ttf", 40)
            
        screen.fill(GRAY)

        pygame.draw.rect(screen, DARK_GREEN, replay_box)
        pygame.draw.rect(screen, BLACK, replay_box, 3)
        screen.blit(replay_surf, replay_rect)

        pygame.draw.rect(screen, DARK_GREEN, end_box)
        pygame.draw.rect(screen, BLACK, end_box, 3)
        screen.blit(end_surf, end_rect)

        if player1_score == 3:

            winner_text_p1_surf = winner_font.render(f"WINNER {player1_name}", True, BLACK)
            winner_text_p1_rect = winner_text_p1_surf.get_rect(center = (500, 300))
            screen.blit(winner_text_p1_surf, winner_text_p1_rect)

        if player2_score == 3:

            winner_text_p2_surf = winner_font.render(f"WINNER {player2_name}", True, BLACK)
            winner_text_p2_rect = winner_text_p2_surf.get_rect(center = (500, 300))
            screen.blit(winner_text_p2_surf, winner_text_p2_rect)

        if replay_box_hover:
            pygame.draw.rect(screen, GREEN, replay_box)
            pygame.draw.rect(screen, BLACK, replay_box, 3)
            screen.blit(replay_surf, replay_rect)

        if end_box_hover:
            pygame.draw.rect(screen, GREEN, end_box)
            pygame.draw.rect(screen, BLACK, end_box, 3)
            screen.blit(end_surf, end_rect)

        pygame.display.update()
        clock.tick(60)