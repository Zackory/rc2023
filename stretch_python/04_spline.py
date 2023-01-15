import time
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

# Define the waypoints
times = [0.0, 10.0, 20.0]
positions = [robot.arm.status['pos'], 0.45, 0.0]
velocities = [robot.arm.status['vel'], 0.0, 0.0]

# Create the spline trajectory
for waypoint in zip(times, positions, velocities):
    robot.arm.trajectory.add(waypoint[0], waypoint[1], waypoint[2])

# Begin execution
robot.arm.follow_trajectory()
robot.push_command()
time.sleep(0.1)

# Wait until completion
while robot.arm.is_trajectory_active():
    print('Execution time: %f' % robot.arm.get_trajectory_time_remaining())
    time.sleep(0.1)

robot.stop()
