import random
import sys
import pygame

width = 800
height = 600
player_size = 50
player_speed = 1
enemy_size = 30
enemy_speed = 0.5
enemy_count = 5


player_pos = [width/2, height-player_size]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0,width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("raider")

def draw_objects():
    count = 0
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (player_pos[0], player_pos[1],player_size, player_size))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (enemy_pos[0], enemy_pos[1],enemy_size, enemy_size))
        if enemy_pos[1] >= height:
            count += 1
    return count


def update_enemy():
    for i in range (len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, width - enemy_size)
            enemy_list[i][1] = random.randint(-100, 0)


def collision_detection():
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + enemy_size)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + player_size)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + enemy_size)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + player_size)):
            return True
        return False


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed
        return False
score = 0
game_over = False
while not game_over:
    game_over = handle_events()
    update_enemy()
    if collision_detection():
        game_over = True
    score += draw_objects()
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, (255,255,255))
    screen.blit(text, (10,10))
    pygame.display.update()

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", 1, (255, 0, 0))
    screen.blit(text, (width / 2 - 150, height / 2 - 50))
    font = pygame.font.Font(None, 36)
    score_text = font.render("Final Score: " + str(score), 1, (255, 255, 255))
    screen.blit(score_text, (width / 2 - 80, height / 2 + 20))
            
    pygame.display.update()
    pygame.time.delay(2000)
pygame.quit()