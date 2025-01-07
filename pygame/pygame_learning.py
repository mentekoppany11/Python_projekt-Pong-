import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('pygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('pygame/graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('pygame/graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('pygame/graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#        if event.type == pygame.MOUSEMOTION:
#            if player_rectangle.collidepoint(event.pos): print('collision')
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_SPACE:




    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    screen.blit(score_surf,score_rect)
    
    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0: snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_SPACE]:
#        print('jump')

#    if player_rectangle.colliderect(snail_rectangle):
#        print("collide")
#
#    mouse_pos = pygame.mouse.get_pos()
#    if player_rectangle.collidepoint((x,y)):
#        pygame.mouse.get_pressed()


    pygame.display.update()
    clock.tick(60)