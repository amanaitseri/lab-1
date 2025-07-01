import pygame as pg#importing libs
import time

lt = time.localtime()#time setting
ats = int(time.strftime("%S", lt))
atm =int(time.strftime("%M", lt))

def lit(im,rect):
    im.set_colorkey((0,0,0))
    screen.blit(im,rect)
def rotate(surface, angle, pivot, ofs):
    r_im = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    r_ofs= ofs.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = r_im.get_rect(center=pivot+r_ofs)
    return r_im, rect  # Return the rotated image and shifted rect.

pg.init()#pygame init
screen = pg.display.set_mode((800, 800))#screen create
clock = pg.time.Clock()
pivot = (400, 400)#start positions for strelki
pivot1 =(400, 400)
ofs = pg.math.Vector2((-195//2)+21, (-165//2)+21)#ofset for images
ofs1 = pg.math.Vector2((-251//2)+21, (-168//2)+21)
angle = 0+6*atm+54
angle1 = 3+6*ats+48#angle setting for strelkas
bgim = pg.image.load('back.jpeg')#loading images
im = pg.image.load('minutes.jpeg').convert_alpha()
im1 = pg.image.load('seconds.jpeg').convert_alpha()#
run = True
while run:#game loop
    for event in pg.event.get():#event check
        if event.type == pg.QUIT:
            run = False
            
    angle += 1/10# angle increase
    r_im, rect = rotate(im, angle, pivot, ofs)
    angle1 += 6 
    r_im1, rect1 = rotate(im1, angle1, pivot1, ofs1)#rotate images of strelkas to increased angle
    screen.blit(bgim,(0,0))
    lit(r_im,rect)#bliting images
    lit(r_im1,rect1)
    pg.display.update()#update screen
    clock.tick(1)#time sett
   
pg.quit()#quit if game loop break