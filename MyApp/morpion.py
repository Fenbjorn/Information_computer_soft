import pygame
import sys


class grid_game:
    def __init__(self, screen):
        self.screen = screen
        self.lines = [((200, 0), (200, 600)), ((400, 0), (400, 600)), ((0, 200), (600, 200)), ((0, 400), (600, 400)), ]

    def show(self):
        for lines in self.lines:
            pygame.draw.line(self.screen, (0, 0, 0), lines[0], lines[1], 2)


class game:

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Morpion')
        self.game_on = True
        self.grid_game = grid_game(self.screen)

    def game_event(self):
        while self.game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Event du click
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    # position de la souris
                    position = pygame.mouse.get_pos()
                    print(position)

            self.screen.fill((240, 240, 240))
            self.grid_game.show()

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game().game_event()
    pygame.quit()
