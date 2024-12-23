import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_width = bg_img.get_width()

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)

    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        bg_x = (bg_x - 1) % bg_width

        key_lst = pg.key.get_pressed()
        move_x, move_y = 0, 0  


        if key_lst[pg.K_UP]:
            move_y -= 1
        if key_lst[pg.K_DOWN]:
            move_y += 1
        if key_lst[pg.K_LEFT]:
            move_x -= 1
        if key_lst[pg.K_RIGHT]:
            move_x += 1
        else:
            move_x -= 1

        kk_rct.move_ip(move_x, move_y)

        screen.blit(bg_img, [bg_x - bg_width, 0])  
        screen.blit(bg_img, [bg_x, 0])  

        screen.blit(kk_img, kk_rct)

        pg.display.update()
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
