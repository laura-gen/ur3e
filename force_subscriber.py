# On récupère la force et le torque du robot ur3e

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped 
import time

class ForceSubs(Node):

    def __init__(self):
        super().__init__("print_force")
        self.force_subscriber = self.create_subscription(WrenchStamped,"/force_torque_sensor_broadcaster/wrench",self.force_callback,10)
        self.last_log_time = time.time()  # Temps initial
        self.log_interval = 1.0  # En secondes

    def force_callback(self, msg: WrenchStamped):
        if (time.time() - self.last_log_time) >= self.log_interval:
            self.get_logger().info("force x:" + str(msg.wrench.force.x) + " N  " + "force y:" + str(msg.wrench.force.y) + " N  " + "force z:" + str(msg.wrench.force.z) + " N  ")
            self.get_logger().info("torque x:" + str(msg.wrench.torque.x) + " N/m  " + "torque y:" + str(msg.wrench.torque.y) + " N/m  " + "torque z:" + str(msg.wrench.torque.z) + " N/m")
            self.last_log_time = time.time()

def main(args=None):
    rclpy.init(args=args)
    node = ForceSubs() 
    rclpy.spin(node)
    rclpy.shutdown()
