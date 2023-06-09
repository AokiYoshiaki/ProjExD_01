import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ProjExD2023/ex01-20230418/fig/pg_bg.jpg")

    tmr = 0
    x=0
    y=0

    kk_imgbase=pg.image.load("ProjExD2023/ex01-20230418/fig/3.png")
    kk_img=pg.transform.flip(kk_imgbase,True,False)
    kk_imgs=[kk_img,pg.transform.rotozoom(kk_img,10,1.0)]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        if tmr % 50==0:
            if x==1:
                x=0
            else:
                x=1
        if tmr == 3200:
            tmr=0
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[1600-tmr,0])
        screen.blit(bg_img,[3200-tmr,0])
        screen.blit(kk_imgs[x],[300,200])
        
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()