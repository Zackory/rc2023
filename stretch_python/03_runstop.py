import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.arm.move_to(0.0)
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.arm.move_to(0.5)
robot.push_command()

# Runstop motion midway through the motion
input('Hit enter to runstop motion')
robot.pimu.runstop_event_trigger() # pimu = Power+IMU
robot.push_command()

input('Hit enter to restart motion')    
robot.pimu.runstop_event_reset()
robot.push_command()

robot.stop()
