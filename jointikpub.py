#-------------------------------------
# Temp, IK tester v01
#-------------------------------------
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout

class IKPublisher(Node):
    def __init__(self):
        super().__init__('ik_slider')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)

    def publish_angles(self, theta1, theta2, theta3):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['joint1', 'joint2', 'joint3']
        msg.position = [theta1, theta2, theta3]
        self.publisher.publish(msg)

def ik_solver(x, y):
    # Test: planar 2‑link IK, extend for 3‑DOF later........
    L1, L2 = 0.3, 0.25
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2)/(2*L1*L2)
    theta2 = math.acos(cos_theta2)
    theta1 = math.atan2(y, x) - math.atan2(L2*math.sin(theta2), L1+L2*math.cos(theta2))
    theta3 = 0.0  # wrist straight
    return theta1, theta2, theta3

class SliderGUI(QWidget):
    def __init__(self, node):
        super().__init__()
        self.node = node
        layout = QVBoxLayout()
        self.slider_x = QSlider()
        self.slider_y = QSlider()
        layout.addWidget(self.slider_x)
        layout.addWidget(self.slider_y)
        self.setLayout(layout)
        self.slider_x.valueChanged.connect(self.update)
        self.slider_y.valueChanged.connect(self.update)

    def update(self):
        x = self.slider_x.value()/100.0
        y = self.slider_y.value()/100.0
        theta1, theta2, theta3 = ik_solver(x, y)
        self.node.publish_angles(theta1, theta2, theta3)

def main():
    rclpy.init()
    node = IKPublisher()
    app = QApplication(sys.argv)
    gui = SliderGUI(node)
    gui.show()
    app.exec_()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
