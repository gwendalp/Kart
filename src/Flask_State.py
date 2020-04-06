#! /usr/bin/env python

import os
import rospy
import threading

from flask import Flask

from std_msgs.msg import Float64

def ros_callback(msg):
    print(msg)

threading.Thread(target=lambda: rospy.init_node('REST_node', disable_signals=True)).start()
rospy.Subscriber('/listener', Float64, ros_callback)
pub = rospy.Publisher('/talker', Float64, queue_size=10)

app = Flask(__name__)

@App.route('/')
def hello_world():
    msg = Float64()
    msg.data = 1.0
    pub.publish(msg)

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host=os.environ['ROS_IP'], port=3000)