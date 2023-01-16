import rospy, sys
import stretch_body.robot
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
rospy.init_node('speech')

def callback(msg):
    transcript = ' '.join(map(str, msg.transcript))
    print(transcript)
    # Do something with the text
    sys.exit(0)

sub = rospy.Subscriber('speech_to_text', SpeechRecognitionCandidates, callback)
rospy.spin()
