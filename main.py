import sys, pygame, os, time


FPS = 60
BLACK = (0, 0, 255)
running = True

pygame.init()
size = width, height = 600, 300
pygame.display.set_caption('Game over')
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

gameoverbar = load_image('gameover.png')
go_sprite = pygame.sprite.Sprite(all_sprites)
go_sprite.image = gameoverbar
go_sprite.rect = go_sprite.image.get_rect()
go_sprite.rect.right = -go_sprite.rect.size[-1]
sfx = pygame.mixer_music.load('data/sound.wav')
pygame.mixer_music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not (go_sprite.rect.right == width):
        go_sprite.rect.right += 10
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
