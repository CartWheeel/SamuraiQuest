# game set up
WIDTH    = 1280 # adjustable width
HEIGHT   = 720  # and height
FPS      = 60
TILESIZE = 32

# ui
BAR_HEIGHT = 12
HEALTH_BAR_WIDTH = 300
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = '../my_graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general collors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#CDD7D6'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = '#F64F3C'
ENERGY_COLOR = '#5B91D7'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111' 
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE' 

weapon_data = {
    'katana': {'cooldown': 100, 'damage': 10, 'graphic':'../my_graphics/weapons/katana/full.png'}
}

# magic
magic_data = {
    'shuriken' : {'strength': 5, 'cost': 5, 'graphic': '../my_graphics/particles/shuriken/shuriken.png'},
    'heal'     : {'strength': 20, 'cost': 10, 'graphic': '../my_graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'shade'  : {'health': 200,'exp': 500,'damage': 25,'attack_type': 'thunder','attack_sound': '','speed': 2,'resistance': 5,'attack_radius': 60,'notice_radius': 150},
    'kitsune': {'health': 100,'exp': 100,'damage': 15,'attack_type': 'claw','attack_sound': '','speed': 3,'resistance': 3,'attack_radius': 40,'notice_radius': 200},
    'bamboo' : {'health': 50,'exp': 50,'damage': 5,'attack_type': 'leaf_attack','attack_sound': '','speed': 1,'resistance': 3,'attack_radius': 20,'notice_radius': 100},
    'shade_alt'  : {'health': 200,'exp': 100,'damage': 25,'attack_type': 'thunder','attack_sound': '','speed': 2,'resistance': 5,'attack_radius': 60,'notice_radius': 150},
    'kitsune_alt': {'health': 100,'exp': 50,'damage': 15,'attack_type': 'leaf_attack','attack_sound': '','speed': 3,'resistance': 3,'attack_radius': 40,'notice_radius': 200}
}