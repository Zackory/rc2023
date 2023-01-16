import rospy, tf
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

rospy.init_node('transformations')
listener = tf.TransformListener()
from_frame_rel = 'base_link'
to_frame_rel = 'link_grasp_center'

rospy.sleep(1.0)
rate = rospy.Rate(1)

robot.arm.move_to(0.5)
robot.push_command()

while not rospy.is_shutdown():
    try:
        translation, rotation = listener.lookupTransform(to_frame_rel, from_frame_rel, rospy.Time(0))
        rospy.loginfo('The pose of target frame %s with respect to %s is: \n %s, %s', to_frame_rel, from_frame_rel, translation, rotation)
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        continue
    rate.sleep()
