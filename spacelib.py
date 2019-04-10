import sys
import pygame

#local imports
from alglib import Vector2 

class GameObject():
    """Game fundamental interactive block"""
    def __init__(self, layer_id, position, size, **kwargs):
        """layer_id : str
           position : tuple
           size     : tuple 
        """
        self.layer_id = layer_id #layer name
        self.rect = pygame.rect.Rect(position, size)
        self.attrs = kwargs 
        self.vec_pos = Vector2(position[0], position[1]) #vector position in relation to (left, top)

        self.alive = True

        self.update_rect_pos() #updates position

    def tofu_blit(self, surface):
        """draws a tofu (rectangle) image onto the surface
            surface : pygame.Surface
        """
        pygame.draw.rect(surface, self.attrs['color'], self.rect)
        #obs: the drawn position will be the vector position (vec_pos)
        #in relation to (left, top) surface position

    def update_rect_pos(self):
        """updates rect position to vector position"""
        self.rect.center = self.vec_pos.x, self.vec_pos.y

class Player(GameObject):
    """player game object"""
    def __init__(self, layer_id, position, size, **kwargs):
        super().__init__(layer_id, position, size, **kwargs)
    
    def move(self, time, move_tag):
        """Moves the player
           time : float in seconds (s)
           move_tag : 'i', 'l', 'r', 'u', 'd' 
        """
        
        uni_x = Vector2(1, 0)
        uni_y = Vector2(0, 1)

        if move_tag == 'r':
            self.vec_pos = self.vec_pos + uni_x * time * self.attrs['speed']
        if move_tag == 'l':
            self.vec_pos = self.vec_pos - uni_x * time * self.attrs['speed']
        if move_tag == 'u':
            self.vec_pos = self.vec_pos - uni_y * time * self.attrs['speed']
        if move_tag == 'd':
            self.vec_pos = self.vec_pos + uni_y * time * self.attrs['speed']
        
        self.update_rect_pos()

class Bullet(GameObject):
    """bullet game object"""
    def __init__(self, layer_id, position, size, lifetime,**kwargs):
        super().__init__(layer_id, position, size, **kwargs)
        self.lifetime = lifetime 
        self.time_counter = 0
    
    def move(self, time):
        self.time_counter += time #adds time 
        if self.time_counter >= self.lifetime:
            self.alive = False










