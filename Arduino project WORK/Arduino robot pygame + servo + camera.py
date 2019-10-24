from Robot import Motors
import pygame as pg
import pygame.camera as wc

robot = Motors([4,2,8,7])
pg.init()
wc.init()
window = pg.display.set_mode((640,480),0)
Video = wc.Camera(wc.list_cameras()[0],(640,480))
Video.start()

while True:
    frame = Video.get_image()
    frame = pg.transform.scale(frame,(640,480))
    window.blit(frame,(0,0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
##################################################################
            if event.key == pg.K_w:
                robot.Forward()
                print(robot.status)
            elif event.key == pg.K_s:
                robot.Backward()
                print(robot.status)
            elif event.key == pg.K_a:
                robot.Turnleft()
                print(robot.status)
            elif event.key == pg.K_d:
                robot.Turnright()
                print(robot.status)
            elif event.key == pg.K_e:
                robot.Rightmotorforward()
                print(robot.status)
            elif event.key == pg.K_c:
                robot.Rightmotorbackward()
                print(robot.status)
            elif event.key == pg.K_q:
                robot.Leftmotorforward()
                print(robot.status)
            elif event.key == pg.K_z:
                robot.Leftmotorbackward()
                print(robot.status)
            if event.key == pg.K_LEFT:
                robot.Servoplus(-5)
                print(robot.status)
            elif event.key == pg.K_RIGHT:
                robot.Servoplus(5)
                print(robot.status)
##################################################################
            if event.key == pg.K_ESCAPE:
                Video.stop()
                pg.quit()
        elif event.type == pg.KEYUP:
            print("Stop")
            robot.Stop()
