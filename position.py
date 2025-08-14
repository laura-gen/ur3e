# On initialise le robot ur3e à une certaine position.
# Commande pour initialiser les joints aux positions [32, -84, 90, -138, -118, 179] : ros2 topic pub /joints_position trajectory_msgs/JointTrajectory "{joint_names: [], points: [{positions: [32, -84, 90, -138, -118, 179], time_from_start: {sec: 3}}]}"

import rclpy 
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math

class Position(Node):

    def __init__(self):
        super().__init__("initialize_position")
        
        self.pose_subscriber_ = self.create_subscription(JointTrajectory,"/joints_position",self.pose_callback,10)  
        self.pose_publisher_= self.create_publisher(JointTrajectory, "/joint_trajectory_controller/joint_trajectory", 10) 

    def pose_callback(self):
        msg = JointTrajectory()
        msg.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
        positions_deg = msg
        positions_rad = []
        point = JointTrajectoryPoint()
        point.time_from_start.sec = 3 # la position finale doit etre atteinte au bout de 3 secondes 
        msg.points.append(point)
        for i in positions_deg : 
            positions_rad.append(math.radians(i)) # Conversion des degrés en radians 
        for i in range (6):
            msg.points[0].positions.append(positions_rad[i])

        self.pose_publisher_.publish(msg)
        self.get_logger().info("positions sent.") 
        print(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Position() 
    rclpy.spin(node)
    rclpy.shutdown()
