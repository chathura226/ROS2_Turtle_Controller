#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello")

def main(args=None):
    # initializing ros2 communications
    rclpy.init(args=args) 

    node=MyNode()

    #continue to run indefinitely - keep node alive
    rclpy.spin(node)
    # shutting down ros2 comms
    rclpy.shutdown()


if __name__=='__main__':
    main()