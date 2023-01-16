import rospy, sys, cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
rospy.init_node('rgb')
bridge = CvBridge()

def callback(msg):
    try:
        image = bridge.imgmsg_to_cv2(msg, 'bgr8')
        # Do something with your image
        cv2.imshow('image', image)
        cv2.waitKey(3)
    except CvBridgeError as e:
        rospy.logwarn('CV Bridge error: {0}'.format(e))

sub = rospy.Subscriber('/camera/color/image_raw', Image, callback, queue_size=1)
rospy.spin()
