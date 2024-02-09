import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon

class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visable_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None

        #sprite setup
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary'      : import_csv_layout('../my_map/map_FloorBlocks.csv'),
            'grass'         : import_csv_layout('../my_map/map_Grass.csv'),
            'object_collide': import_csv_layout('../my_map/map_ObjectsCollide.csv'),
            'object_detail1': import_csv_layout('../my_map/map_ObjectsDetail1.csv'),
            'object_detail2': import_csv_layout('../my_map/map_ObjectsDetail2.csv'),
            
        }
        graphics = {
            'grass'  : import_folder('../my_graphics/grass'),
            'objects': import_folder('../my_graphics/objects') # path here
        }
        
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible') # include self.visable_sprites to make boundary visable
                        
                        # create grass tiles
                        if style == 'grass':                            
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y), [self.visable_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        
                        # create an collisionable object tiles
                        if style == 'object_collide':                            
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visable_sprites,self.obstacle_sprites], 'object_collide',surf)
                        
                        # create layer 1 object tiles
                        if style == 'object_detail1':                    
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visable_sprites], 'object_detail1',surf)
                        
                        # create layer 2 object tiles
                        if style == 'object_detail2':                          
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visable_sprites], 'object_detail12',surf)

                if col == 'x':
                    Tile((x, y), [self.visable_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visable_sprites],self.obstacle_sprites)
        
        self.player = Player((700, 550), [self.visable_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visable_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # update and draw the game
        self.visable_sprites.custom_draw(self.player)
        self.visable_sprites.update()
        debug(self.player.status)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # zoom
        self.zoom_scale = 3
        self.internal_surf_size = (1200,1200)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_width, self.half_height))
        self.internal_surf_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_width
        self.internal_offset.y = self.internal_surf_size[0] // 2 - self.half_height


        # creating the floor
        self.floor_surf = pygame.image.load('../my_graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    # def zoom_keyboard_controls(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_q]:
    #         self.zoom_scale += 0.1
    #     if keys[pygame.K_e]:
    #         self.zoom_scale -= 0.1

    def custom_draw(self,player):
        # keyboard zoom control
        # self.zoom_keyboard_controls()

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image,offset_pos)

        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surf_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_width, self.half_height))

        self.display_surface.blit(scaled_surf, scaled_rect)