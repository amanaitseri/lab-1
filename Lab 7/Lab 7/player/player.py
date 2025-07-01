import sys, pygame, os
import time

pygame.init()

# display
screen = pygame.display.set_mode((666, 500))

back = pygame.image.load('bac.png')
back = pygame.transform.scale(back, (666, 500))
screen.blit(back, (0, 0))
pygame.display.update()


# muzika
mus = [
    'tsis7_player_music_al-fakher-muzykadljadushi-mp3.mp3',
    '1.mp3',
    '2.mp3'
]
index = 0
path = '{}'
pygame.mixer.music.load(path.format(mus[index]))


pygame.mixer.music.load(path.format(mus[index]))
isPlaying = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_e]:
        isPlaying = True
        pygame.mixer.music.play()

    if key[pygame.K_q]:
        isPlaying = False
        pygame.mixer.music.stop()

    if key[pygame.K_SPACE]:
        if isPlaying:
            pygame.mixer.music.pause()
            isPlaying = False
        else:
            pygame.mixer.music.unpause()
            isPlaying = True

    if key[pygame.K_RIGHT]:
        index += 1
        if index == len(mus):
            index = 0

        pygame.mixer.music.load(path.format(mus[index]))
        pygame.mixer.music.play()

    if key[pygame.K_LEFT]:
        index -= 1
        if index < 0:
            index = len(mus) - 1

        pygame.mixer.music.load(path.format(mus[index]))
        pygame.mixer.music.play()

    time.sleep(0.2)

"""
management

E-start player
Q-stop player
Space-pause
right arrow(->)-next 
left arrow(<-)-previous

"""