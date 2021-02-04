import os, sys
import pygame
import simplejson


def main():
    args = sys.argv[1:]

    pygame.init()

    clock = pygame.time.Clock()

    size = width, height = 640, 400

    internal_size = internal_width, internal_height = 320, 200

    black = 0, 0, 0

    fsex = pygame.font.Font("fsex300.ttf", 16)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("dgafTech Engine - Demo 0.0.1 - Bouncing ASCII Dude")

    backbuffer = pygame.Surface(internal_size)

    dude = pygame.image.load("dude.png").convert()
    pygame.display.set_icon(pygame.transform.scale(dude, [32, 32]))

    # set colorkey after setting icon
    dude.set_colorkey(black)

    dude_rect = dude.get_rect()

    x_delta = 1

    y_delta = 1

    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        fps = int(clock.get_fps())

        dude_rect = dude_rect.move([x_delta, y_delta])

        if dude_rect.left < 0 or dude_rect.right > internal_width:
            x_delta = -x_delta
        if dude_rect.top < 0 or dude_rect.bottom > internal_height:
            y_delta = -y_delta

        screen.fill(black)

        backbuffer.fill(black)

        backbuffer.blit(dude, dude_rect)

        backbuffer.blit(fsex.render("FPS: " + str(fps), False, [255, 255, 255]), [8, 8])

        screen.blit(pygame.transform.scale(backbuffer, [width, height]), [0, 0, width, height])



        clock.tick(60)

        pygame.display.flip()

if __name__ == "__main__":
    main()
