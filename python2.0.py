from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
import argparse

parse_panda_controls = argparse.ArgumentParser()
parse_panda_controls.add_argument('--spinCamera', '--sc', type=str,
                                  help="True or False whether to spin the camera or not", default=True)
parse_panda_controls.add_argument('--animatePanda', '--ap', type=str,
                                  help="True or False whether to spin the camera or not", default=True)
parse_panda_args = parse_panda_controls.parse_args()
print(parse_panda_args.spinCamera)

allow_spin = True
allow_Panda_Animate = True

try:

    if int(parse_panda_args.spinCamera) >= 1 or parse_panda_args.spinCamera.lower() == "true":
        print(parse_panda_args.spinCamera, "true1")
        allow_spin = True

    elif int(parse_panda_args.spinCamera) <= 0 or parse_panda_args.spinCamera.lower() == "false":
        print(parse_panda_args.spinCamera, "false1")
        allow_spin = False
    else:
        print("The values you entered for --sc or --spinCamera (", parse_panda_args.spinCamera,
              ") are not supported. Please enter either Boolean values(True/False) or integer values ( >1 is true )")
        exit()
except ValueError:
    if parse_panda_args.spinCamera.lower() == "true":
        print(parse_panda_args.spinCamera, "true1")
        allow_spin = True

    elif parse_panda_args.spinCamera.lower() == "false":
        print(parse_panda_args.spinCamera, "false1")
        allow_spin = False
    else:
        print("The values you entered for --sc or --spinCamera (", parse_panda_args.spinCamera,
              ") are not supported. Please enter either Boolean values(True/False) or integer values ( >1 is true )")
        exit()

try:
    if int(parse_panda_args.animatePanda) >= 1 or parse_panda_args.animatePanda.lower() == "true":
        print(parse_panda_args.animatePanda, "true2")
        allow_Panda_Animate = True

    elif int(parse_panda_args.animatePanda) <= 0 or parse_panda_args.animatePanda.lower() == "false":
        print(parse_panda_args.animatePanda, "false2")
        allow_Panda_Animate = False
    else:
        print("The values you entered for --ap or --animatePanda (", parse_panda_args.animatePanda,
              ") are not supported. Please enter either Boolean values(True/False) or integer values ( >1 is true )")
        exit()
except ValueError:
    if parse_panda_args.animatePanda.lower() == "true":
        print(parse_panda_args.animatePanda, "true2")
        allow_Panda_Animate = True

    elif parse_panda_args.animatePanda.lower() == "false":
        print(parse_panda_args.animatePanda, "false2")
        allow_Panda_Animate = False
    else:
        print("The values you entered for --ap or --animatePanda (", parse_panda_args.animatePanda,
            ") are not supported. Please enter either Boolean values(True/False) or integer values ( >1 is true )")
        exit()

class MyAp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add 3d panda. Not if executed false command
        if allow_Panda_Animate == True:
            self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005)
            self.pandaActor.reparentTo(self.render)
            # Loop panda animation
            self.pandaActor.loop("walk")

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")


        nature_sound = self.loader.loadSfx("nature.mp3")
        nature_sound.setLoop(True)
        nature_sound.play()

        if allow_Panda_Animate == True:
            bear = self.loader.loadSfx("bear.mp3")
            bear.setLoop(True)
            bear.play()

    # move camera. Not if executed false command
    def spinCameraTask(self, task):
        if allow_spin == True:
            angleDegrees = task.time * 6.0
        elif allow_spin == False:
            angleDegrees = 1

        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

MyAp().run()
