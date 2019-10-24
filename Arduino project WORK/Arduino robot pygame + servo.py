from Robot import Motors
import pygame as kb

robot = Motors([4,2,8,7])
kb.init()
kb.display.set_mode((100,100),0)

while True:
    for event in kb.event.get():
        if event.type == kb.KEYDOWN:
##################################################################
            if event.key == kb.K_w:
                robot.Forward()
                print(robot.status)
            elif event.key == kb.K_s:
                robot.Backward()
                print(robot.status)
            elif event.key == kb.K_a:
                robot.Turnleft()
                print(robot.status)
            elif event.key == kb.K_d:
                robot.Turnright()
                print(robot.status)
            elif event.key == kb.K_e:
                robot.Rightmotorforward()
                print(robot.status)
            elif event.key == kb.K_c:
                robot.Rightmotorbackward()
                print(robot.status)
            elif event.key == kb.K_q:
                robot.Leftmotorforward()
                print(robot.status)
            elif event.key == kb.K_z:
                robot.Leftmotorbackward()
                print(robot.status)
            if event.key == kb.K_LEFT:
                robot.Servoplus(-5)
                print(robot.status)
            elif event.key == kb.K_RIGHT:
                robot.Servoplus(5)
                print(robot.status)
##################################################################
            if event.key == kb.K_ESCAPE:
                kb.quit()
        elif event.type == kb.KEYUP:
            print("Stop")
            robot.Stop()
