'''
Code skeleton Activity 1
'''
import tkinter as tk
import numpy as np
from tutorial7_oop.robot_helper import initialise
import math
# Set a seed for reproducibility
np.random.seed(0)

class Bot:

    def __init__(self,canvasp,object_name=None,):
        self.x = np.random.randint(100, 900)
        self.y = np.random.randint(100, 900)
        self.theta = np.random.uniform(0.0, 2.0 * math.pi)
        #self.theta = 0
        self.name = object_name
        self.ll = 60 #axle width
        self.vl = 0.0
        self.vr = 0.0
        self.battery = 1000
        self.turning = 0
        self.moving = np.random.randint(50, 101)
        self.currentlyTurning = False
        self.canvas = canvasp


    def draw(self):


        angle = np.pi / 2.0
        points = [
            (self.x + 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            (self.x + 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            ]
        self.canvas.create_polygon(points, fill="blue", tags=self.name)

        self.sensorPositions = [
            (self.x + 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y - 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            (self.x - 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y + 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            ]

        centre1PosX = self.x
        centre1PosY = self.y
        self.canvas.create_oval(centre1PosX-15,centre1PosY-15, \
                                centre1PosX+15,centre1PosY+15, \
                                fill="gold",tags=self.name)

        # Generate the battery text
        self.canvas.create_text(self.x,self.y,text=str(self.battery),tags=self.name)

        wheel1PosX = self.x - 30*math.sin(self.theta)
        wheel1PosY = self.y + 30*math.cos(self.theta)
        self.canvas.create_oval(wheel1PosX-3,wheel1PosY-3, \
                                wheel1PosX+3,wheel1PosY+3, \
                                fill="red",tags=self.name)

        wheel2PosX = self.x + 30*math.sin(self.theta)
        wheel2PosY = self.y - 30*math.cos(self.theta)
        self.canvas.create_oval(wheel2PosX-3,wheel2PosY-3, \
                                wheel2PosX+3,wheel2PosY+3, \
                                fill="green",tags=self.name)

        sensor1PosX = self.sensorPositions[0]
        sensor1PosY = self.sensorPositions[1]
        sensor2PosX = self.sensorPositions[2]
        sensor2PosY = self.sensorPositions[3]
        self.canvas.create_oval(sensor1PosX-3,sensor1PosY-3, \
                                sensor1PosX+3,sensor1PosY+3, \
                                fill="yellow",tags=self.name)
        self.canvas.create_oval(sensor2PosX-3,sensor2PosY-3, \
                                sensor2PosX+3,sensor2PosY+3, \
                                fill="yellow",tags=self.name)


def main():
    window = initialise(tk.Tk())
    noOfBots = 30
    for i in range(0,noOfBots):
        bot = Bot(window,object_name="Bot"+str(i), )
        bot.draw()

    window.mainloop()

if __name__ == "__main__":
    main()