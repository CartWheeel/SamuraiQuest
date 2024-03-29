import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        scale_factor = .5
        self.frames = {
			# magic
			'shuriken': import_folder('../my_graphics/particles/shuriken/frames'),
            'shuriken2': self.reflect_images(import_folder('../my_graphics/particles/shuriken/frames')),
			'aura': import_folder('../my_graphics/particles/aura'),
			'heal': import_folder('../my_graphics/particles/heal/frames'),
			
			# attacks 
			'claw': import_folder('../my_graphics/particles/claw'),
			'slash': import_folder('../my_graphics/particles/slash'),
			'sparkle': import_folder('../my_graphics/particles/sparkle'),
			'leaf_attack': import_folder('../my_graphics/particles/leaf_attack'),
			'thunder': import_folder('../my_graphics/particles/thunder'),

			# monster deaths
			'kitsune': import_folder('../my_graphics/particles/smoke_orange'),
			'shade': import_folder('../my_graphics/particles/smoke'),
			'bamboo': import_folder('../my_graphics/particles/bamboo'),
			
			# leafs 
			'leaf': (
				import_folder('../my_graphics/particles/leaf1'),
				import_folder('../my_graphics/particles/leaf2'),
				import_folder('../my_graphics/particles/leaf3'),
				import_folder('../my_graphics/particles/leaf4'),
				import_folder('../my_graphics/particles/leaf5'),
				import_folder('../my_graphics/particles/leaf6'),
				self.reflect_images(import_folder('../my_graphics/particles/leaf1')),
				self.reflect_images(import_folder('../my_graphics/particles/leaf2')),
				self.reflect_images(import_folder('../my_graphics/particles/leaf3')),
				self.reflect_images(import_folder('../my_graphics/particles/leaf4')),
				self.reflect_images(import_folder('../my_graphics/particles/leaf5')),
				self.reflect_images(import_folder('../my_graphics/particles/leaf6'))
				)
			}
    
    def reflect_images(self,frames):
        new_frames = []
        
        for frame in frames:
               flipped_frames = pygame.transform.flip(frame,True,False)
               new_frames.append(flipped_frames)               
        return new_frames
    
    def create_grass_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)
        
    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)
    
class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups) -> None:
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.5
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()