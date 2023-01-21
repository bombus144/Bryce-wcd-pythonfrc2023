import wpilib
import wpilib.simulation

import imp
import inspect
import logging
import pathlib
import typing

import hal.simulation
from pyfrc.physics import drivetrains

from wpimath.kinematics import ChassisSpeeds
from wpimath.geometry import Pose2d, Rotation2d, Transform2d, Translation2d, Twist2d

import wpilib.simulation

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units


logger = logging.getLogger("pyfrc.physics")


class PhysicsInitException(Exception):
    pass


class PhysicsEngine:

    def __init__(self, physics_controller: "PhysicsInterface"):
        self.physics_controller = physics_controller
        self.drivetrain = drivetrains.TwoMotorDrivetrain(deadzone=drivetrains.linear_deadzone(0.2))

        self.l_motor = wpilib.simulation.PWMSim(1)
        self.r_motor = wpilib.simulation.PWMSim(2)

    def update_sim(self, now: float, tm_diff: float):
        l_motor = self.l_motor.getSpeed()
        r_motor = self.r_motor.getSpeed()

        speeds = self.drivetrain.calculate(l_motor, r_motor)
        self.physics_controller.drive(speeds, tm_diff)

        # optional: compute encoder
        # l_encoder = self.drivetrain.wheelSpeeds.left * tm_diff
        
        pass