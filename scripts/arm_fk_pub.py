#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import time

class ArmPublisher(Node):
    def __init__(self):
        super().__init__('arm_fk_publisher')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

        # Defining set of points (joint angles in radians)
        self.points = [
            [0.0, 0.0],
            [0.5, 0.5],
            [1.0, -0.5],
            [0.0, 1.0]
        ]
        self.index = 0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['joint1', 'joint2'] 
        msg.position = self.points[self.index]

        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing {msg.position}')

        # Cycling through points...
        self.index = (self.index + 1) % len(self.points)
        time.sleep(1.0)  # pause bw points

def main(args=None):
    rclpy.init(args=args)
    node = ArmPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

