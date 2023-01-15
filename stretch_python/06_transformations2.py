import rospy
from geometry_msgs.msg import TransformStamped
import tf2_ros
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer)

from_frame_rel = 'base_link'
to_frame_rel = 'link_grasp_center'

rospy.sleep(1.0)
rate = rospy.Rate(1)

robot.arm.move_to(0.5)
robot.push_command()

while not rospy.is_shutdown():
    try:
        trans = tf_buffer.lookup_transform(to_frame_rel, from_frame_rel, rospy.Time())
        rospy.loginfo('The pose of target frame %s with respect to %s is: \n %s', to_frame_rel, from_frame_rel, trans.transform)
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        rospy.logwarn(' Could not transform %s from %s ', to_frame_rel, from_frame_rel)
    rate.sleep()
