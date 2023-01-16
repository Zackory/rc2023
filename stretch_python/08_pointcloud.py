import rospy, tf
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointCloud
from geometry_msgs.msg import Point32
rospy.init_node('pc')
listener = tf.TransformListener(True, rospy.Duration(10.0))
listener = tf.TransformListener()
listener.waitForTransform('base_link', 'camera_color_optical_frame', rospy.Time(), rospy.Duration(4.0))

def callback(msg):
    print('msg received')
    temp_cloud = PointCloud()
    temp_cloud.header = msg.header
    print('starting')
    for data in pc2.read_points(msg, skip_nans=True):
        temp_cloud.points.append(Point32(data[0], data[1], data[2]))
    print('done')
    point_cloud = None
    while point_cloud is None:
        try:
            # Transform all points to have 3D positions relative to robot base link
            point_cloud = listener.transformPointCloud('base_link', temp_cloud)
        except (tf.LookupException, tf.ConnectivityException,tf.ExtrapolationException) as e:
            print(e)
            pass
    # Do something with your point cloud
    print(point_cloud)

pointcloud2_sub = rospy.Subscriber('/camera/depth/color/points', PointCloud2, callback, queue_size=1)
rospy.spin()
