import wpilib
from wpilib import XboxController
from wpilib import Talon
import wpilib.drive

class MyRobot(wpilib.TimedRobot):
    # def __init__(self):
    #     motors={}
    #     self.motors = motors
        
    def robotInit(self):
        self.controller = XboxController(0)
        # self.LeftFrontMotor = Talon(0)
        # self.LeftMiddleMotor = Talon(1)
        # self.LeftBackMotor = Talon(3)
        # self.RightFrontMotor = Talon(4)
        # self.RightMiddleMotor = Talon(5)
        # self.RightBackMotor = Talon(6)
        # self.l_motors = wpilib.MotorControllerGroup(self.LeftFrontMotor,self.LeftMiddleMotor,self.LeftBackMotor)
        # self.r_motors = wpilib.MotorControllerGroup(self.RightFrontMotor,self.RightMiddleMotor,self.RightBackMotor)
        
        self.l_motor = Talon(0)
        self.r_motor = Talon(1)
        
        self.drive = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)
        self.stick = wpilib.Joystick(0)

        
        # left_motors = wpilib.MotorControllerGroup()

    def TeleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())

            
if __name__ == "__main__":
    wpilib.run(MyRobot)