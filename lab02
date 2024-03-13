import pygame
import sys
import math

class Transforms2D:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2D Transforms")

        self.clock = pygame.time.Clock()

        # domyslna transformacja
        self.transform_select = 0

    def apply_transforms(self):
        # Lista funkcji transformacji
        transforms = [
            lambda x, y: (x, y),  #transformacja 0
            lambda x, y: (x * 0.5 + 1, y * 0.5 + 1),  #transformacja 1
            lambda x, y: (x * math.cos(math.radians(45)) - y * math.sin(math.radians(45)),
                          x * math.sin(math.radians(45)) + y * math.cos(math.radians(45))),  #transformacja 2
            lambda x, y: (x * 0.5, y),  #transformacja 3
            lambda x, y: (x + 0.4 * y, y),  #transformacja 4
            lambda x, y: (x, y * 0.5 - 200),  #transformacja 5
            lambda x, y: (-y * 0.7, x),  #transformacja 6
            lambda x, y: (x * 0.5, y),  #transformacja 7(taka jak 3)
            lambda x, y: ((x) * math.cos(math.radians(30)) - (y * 0.5 + 110) * math.sin(math.radians(30)),
              (x) * math.sin(math.radians(30)) + (y * 0.5 + 170) * math.cos(math.radians(30))),  #transformacja 8
            lambda x, y: (x + 150, -y * 0.50),  #transformacja 9
        ]

        # Tworzenie wielokata (punktow)
        n = 11
        points = [(150 * math.cos((2 * math.pi / n) * i), 150 * math.sin((2 * math.pi / n) * i)) for i in range(n)]

        # wybieranie funkcji transformacji
        transformed_points = [transforms[self.transform_select](*point) for point in points]

        # przesuniecie punktow do srodka ekranu
        center_x, center_y = self.width // 2, self.height // 2
        transformed_points = [(x + center_x, y + center_y) for x, y in transformed_points]

        return transformed_points

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # Obsluga klawiszy od 0 do 9
                    if pygame.K_0 <= event.key <= pygame.K_9:
                        self.transform_select = event.key - pygame.K_0

            self.screen.fill((255, 255, 255))

            #rysowanie wielokata
            pygame.draw.polygon(self.screen, (0, 0, 200), self.apply_transforms(), 0)

            pygame.display.flip()

            #ustawienie liczby klatke
            self.clock.tick(30)

if __name__ == "__main__":
    app = Transforms2D()
    app.run()

