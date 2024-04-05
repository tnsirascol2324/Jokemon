import pygame
from pytmx.util_pygame import load_pygame
import pyscroll
from player import Player

class Game:
    def __init__(self):
        """
        Initialisation de :
        - Fenêtre, Nom, curseur
        - Groupe de sprites à afficher
        - Posistion du joueur
        - Collisions
        """

        # Création de la fenêtre
        self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        # Définir le nom de la fenêtre
        pygame.display.set_caption("JOKEMON")
        # Rendre le curseur de souris invisible
        pygame.mouse.set_visible(False)
        
        self.running = True

        # Initialisation de la carte
        # Modifier le chemin en fonction du lieu du fichier
        tmx_data = load_pygame('maps/map1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        # Récupération de la position du joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # Initialisation des collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Création d'un groupe de sprites
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def handle_input(self):
        """
        Sortie des inputs et des mouvements du joueurs
        """

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_z] or keys_pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
        elif keys_pressed[pygame.K_q] or keys_pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif keys_pressed[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        if keys_pressed[pygame.K_RALT]:
            self.running = False

    def update(self):
        """
        Update le groupe de sprites
        """
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        """
        Boucle du jeu - ordre de chargement des méthodes
        """

        clock = pygame.time.Clock()

        pygame.init()

        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            # Event de fermeture du jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Bloque les FPS à 60
            clock.tick(60)

            pygame.display.flip()
            
        pygame.quit()