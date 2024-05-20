#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
 
class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.get_logger().info("Turtle Controller has been started!")

    def pose_callback(self,pose:Pose):
        msg=Twist()
        if pose.x>8.0 or pose.x<2.0 or pose.y>8.0 or pose.y<2.0:
            msg.linear.x=1.0
            msg.angular.z=0.9 
            self.cmd_vel_publisher.publish(msg)
            return

        msg.linear.x=5.0
        msg.angular.z=0.0
        self.cmd_vel_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()