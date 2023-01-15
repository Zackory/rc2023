import time
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

# Move to full extension
robot.arm.move_to(0.5)
robot.push_command()
robot.arm.wait_until_at_setpoint() # Wait for motion to complete

# Move the arm backwards by 0.3 meters
robot.arm.move_by(0.3)
robot.push_command()
time.sleep(2.0)

robot.stop()
