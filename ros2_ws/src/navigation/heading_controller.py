#!/usr/bin/env python3
# Heading controller (tidybot-adapted)

import numpy as np
import rclpy
from asl_tb3_lib.control import BaseHeadingController
from asl_tb3_lib.math_utils import wrap_angle
from geometry_msgs.msg import Pose2D, Twist

class HeadingController(BaseHeadingController):
    def __init__(self, node_name: str):
        super().__init__(node_name)
        # self.kp = 2.0
        self.declare_parameter("kp", 2.0)
        
    @property
    def kp(self) -> float:
        return self.get_parameter("kp").value
        
    def compute_control_with_goal(self, current_state: Pose2D, desired_state: Pose2D) -> Twist:
        heading_error = wrap_angle(desired_state.theta - current_state.theta)
        w = self.kp * heading_error
        t = Twist()
        t.angular.z = float(w)
        return t

def main(argv=None):
    rclpy.init(args=argv)
    node = HeadingController("HeadingController")
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__=="__main__":
    main()
