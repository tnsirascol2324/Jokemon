import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        """
        Initialisation de :
        - Sprites du joueur
        - Position de sa hitbox
        """
        super().__init__()
        # Modifier le chemin en fonction du lieu du fichier
        self.sprite_sheet = pygame.image.load('entity/players/player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right':self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 10)
        self.old_position = self.position.copy()
        self.speed = 1.25

    def save_location(self):
        """
        Sauvegarde de la position du joueur
        """ 
        
        self.old_position = self.position.copy()

    def change_animation(self, name): 
        """
        Charge l'image d'animation en fonction de la direction
        """

        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])   
        
    def move_up(self): 
        """
        Vélocité du joueur vers le haut
        """
        self.position[1] -= self.speed
    
    def move_down(self): 
        """
        Vélocité du joueur vers le bas
        """
        self.position[1] += self.speed

    def move_right(self): 
        """
        Vélocité du joueur vers la droite
        """
        self.position[0] += self.speed

    def move_left(self): 
        """
        Vélocité du joueur vers la gauche
        """
        self.position[0] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        """
        Charge la position initiale du joueur
        """
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


    def get_image(self, x, y):
        """
        Récupère les images dans le sprite du joueur
        """
        image = pygame.Surface([32 ,32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image