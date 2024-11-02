import pygame
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 600,800
PLAYER_WIDTH, PLAYER_HEIGHT = 40,40
STAR_WIDTH, STAR_HEIGTH = 10,40
PLAYER_VELOCITY = 2
STAR_VELOCITY = 3

WID = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans",30)


def draw(player, elapsed_time, stars):
    WID.blit(BG, (0,0))

    pygame.draw.rect(WID, "red",player)

    text_time = FONT.render(f"Time: {round(elapsed_time)}s",1,"white")
    WID.blit(text_time, (10,10))

    for star in stars :
        pygame.draw.rect(WID, "white", star)

    pygame.display.update()


def tick():
    time.clock(60)

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_count = 0
    star_add_increment = 2000
    stars = []

    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGTH, STAR_WIDTH, STAR_HEIGTH)
                stars.append(star)
        
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= PLAYER_VELOCITY
        elif keys[pygame.K_RIGHT] and player.x + PLAYER_HEIGHT <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            if star.y + STAR_HEIGTH >= PLAYER_HEIGHT and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            game_over_text = FONT.render(f"YOU LOST YOU LOSER xD",1,"white")
            WID.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2,HEIGHT/2 - game_over_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time,stars)

    pygame.quit()

if __name__ == "__main__":
    main()
