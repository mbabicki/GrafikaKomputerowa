import pygame
import sys

class TransformedShapes:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Drawing With Transforms")
        self.clock = pygame.time.Clock()

    def reset_transform(self):
        self.screen.set_at((0, 0), (255, 255, 255))

    def rectangle(self, center, size, color):
        # Rysuje prostokat o podanych srodku, rozmiarze, kolorze
        pygame.draw.rect(self.screen, color, (center[0] - size[0] // 2, center[1] - size[1] // 2, size[0], size[1]))

    def triangle(self, vertices, color):
        # Rysuje trojkat o podancyh wierzcholkach i kolorze
        pygame.draw.polygon(self.screen, color, vertices)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))

            # Resetuje transformacje
            self.reset_transform()

            # Rysuje prostokat
            self.rectangle((300, 300), (240, 120), (0, 0, 128))


            # obracanie ukladu wspolrzednych o 180stopni
            rotation_matrix = pygame.transform.rotate(pygame.Surface((1, 1)), 180)
            rotated_point = rotation_matrix.get_rect(center=(0, -180)).center
            rotated_triangle = [(point[0] + rotated_point[0], point[1] + rotated_point[1]) for point in [(240, 300), (360, 300), (300, 420)]]
            self.triangle(rotated_triangle, (0, 0, 128))

            # to samo ale w druga strone
            rotation_matrix = pygame.transform.rotate(pygame.Surface((1, 1)), 180)
            rotated_point = rotation_matrix.get_rect(center=(0, 180)).center
            rotated_triangle = [(point[0] + rotated_point[0], point[1] + rotated_point[1]) for point in [(300, 180), (240, 300), (360, 300)]]
            self.triangle(rotated_triangle, (0, 0, 128))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = TransformedShapes()
    app.run()

