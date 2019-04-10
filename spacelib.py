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
    
    def set_attrs(self, attr_dict):
        """kwargs optional initializer
           takes a dict type and sets it as 
            game object attributes  
        """
        self.attrs = attr_dict

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
        """simple bullet movement. Moves bullet to the right 
           time : float in seconds (s) 
        """
        self.time_counter += time #adds time 
        if self.time_counter >= self.lifetime:
            self.alive = False
        
        uni_x = Vector2(1, 0)
        self.vec_pos = self.vec_pos + uni_x * time * self.attrs['speed']

        self.update_rect_pos()

class BulletHandler(GameObject):

    def __init__(self, layer_id, position, bullet_size, bullet_max, bullet_life_time, bullet_attr_dict):
        """Handles all the behaivior of a group of bullets"""
        super().__init__(layer_id, position, bullet_size) #sloppy code here
        
        self.bullet_life_time = bullet_life_time #bullet constrcutor attribute life time 
        self.bullet_attr_dict= bullet_attr_dict #bullet optional (and not so much) attribute dict
        self.bullet_max = bullet_max #maximum bullet capacity
        self.bullet_list = [] #stores all the bullets 

    def shoot_bullet(self):
        """Adds a bullet to the bullet list 
           if is not in maximum capacity 
        """ 
        self.bullet_list.append(Bullet(self.layer_id,\
            tuple(self.vec_pos), self.rect.size, self.bullet_life_time)) #instantiates the a bullet and append to the list of bullets
        self.bullet_list[-1].set_attrs(self.bullet_attr_dict) #takes the last append item and sets its attributes            

        #checks the size of the bullet list
        #if is in the maximum capacity removes the bullet first
        if len(self.bullet_list) > self.bullet_max:
            self.bullet_list = self.bullet_list[1:]
    
    #make threads here 
    def run(self, surface, time):
        for bullet in self.bullet_list:
            bullet.move(time) #moves bullet
            bullet.tofu_blit(surface) #draws bullet

            if not bullet.alive: #if it's dead remove from the list
                self.bullet_list.remove(bullet)






