import pygame

WIDTH, HEIGHT = 700, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super TIC-TAC-TOE")
WHITE = (255,255,255)
BEIGE = (245,245,220)

FPS = 60

def draw_window():
    WIN.fill(BEIGE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()