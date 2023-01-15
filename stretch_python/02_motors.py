import time
import numpy as np
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.arm.move_to(0.5) # Move telescoping arm
robot.lift.move_to(0.4) # Move lift
robot.head.move_by('head_pan', np.radians(45)) # Move head pan
robot.head.move_by('head_tilt', np.radians(45)) # Move head tilt
robot.base.translate_by(0.2) # Move robot base 0.2 meters forward
# robot.base.set_rotational_velocity(v_r=0.1) # You can also set base rotational velocity

# Dexterous wrist and gripper
robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.end_of_arm.move_to('stretch_gripper', 50)

robot.push_command()
time.sleep(5.0)

robot.stop()
