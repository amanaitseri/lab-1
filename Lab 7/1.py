import pygame
pygame.init()

W, H = 800, 800
x = W // 2
y = H // 2
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

mickey = pygame.image.load(r"C:\Users\User\Desktop\W3exercise\TSIS7\main-clock.png")
leftHand = pygame.image.load(r"C:\Users\User\Desktop\W3exercise\TSIS7\left-hand.png")
rightHand = pygame.image.load(r"C:\Users\User\Desktop\W3exercise\TSIS7\right-hand.png")

mickeyRect = mickey.get_rect(center=(x, y))

def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, -angle)  # -angle = по часовой
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect)

start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Время с начала
    elapsed = pygame.time.get_ticks() - start_time
    seconds = (elapsed / 1000) % 60
    minutes = (elapsed / (1000 * 60)) % 60

    rangle = seconds * 6      # 360° / 60с
    langle = minutes * 6      # 360° / 60м

    sc.fill(WHITE)
    sc.blit(mickey, mickeyRect)
    blitRotateCenter(sc, rightHand, (x, y), rangle)
    blitRotateCenter(sc, leftHand, (x, y), langle)

    pygame.display.update()
    clock.tick(60)

   
