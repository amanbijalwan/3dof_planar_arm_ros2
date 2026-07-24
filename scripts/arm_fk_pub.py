#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import numpy as np

class ScaraPublisher(Node):
    def __init__(self):
        super().__init__('scara_fk_publisher')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.05, self.update)

        #points: [joint1, joint2, joint3]
        self.points = [
            [0.0, 0.0, 0.08],
            [0.5, 0.5, -0.08],
            [1.0, -0.5, 0.08],
            [0.0, 1.0, -0.08]
        ]
        self.current = 0
        self.next = 1
        self.steps = 50   #ip steps
        self.step_count = 0

    def update(self):
        # Linear interpolation test
        start = np.array(self.points[self.current])
        end   = np.array(self.points[self.next])
        alpha = self.step_count / self.steps
        pos   = (1 - alpha) * start + alpha * end

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['joint1', 'joint2', 'joint3']
        msg.position = pos.tolist()

        self.pub.publish(msg)

        self.step_count += 1
        if self.step_count > self.steps:
            self.step_count = 0
            self.current = self.next
            self.next = (self.next + 1) % len(self.points)

def main(args=None):
    rclpy.init(args=args)
    node = ScaraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
