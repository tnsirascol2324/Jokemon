import pygame

class Menu:
    def __init__(self):

        # Création de la fenêtre
        self.screen = pygame.display.set_mode((1280, 720))
        # Définir le nom de la fenêtre
        pygame.display.set_caption("JOKEMON")
        pygame.mouse.set_visible(True)
        

        self.menu = True

    
    def input(self):

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        elif keys_pressed[pygame.K_RALT]:
            self.menu = False

        
    def launching(self):

        clock = pygame.time.Clock()

        while self.menu:

            self.input()
            pygame.display.flip()

            # Event de fermeture du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False

            # Bloque les FPS à 60
            clock.tick(60)

            pygame.display.flip()
            
        pygame.quit()